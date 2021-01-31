#!/usr/bin/python3
"""A simple script to get the temperature of an BMP280 sensor over it's I2C interface.
:Author: Vivien Richter
:Version: 1.0.0
:Date: 31/01/2021
:License: `MIT License <https://opensource.org/licenses/MIT>`_
:Based on: `Matt Hawkins <https://bitbucket.org/MattHawkinsUK/rpispy-misc/src/master/python/bme280.py>`_
"""

import smbus
import time
from ctypes import c_short

ADDRESS = 0x76 # Default
REG_DATA = 0xF7
REG_CONTROL = 0xF4
OVERSAMPLE_TEMP = 2
OVERSAMPLE_PRES = 0 # Disabled
MODE = 1 # Forced mode

sensor = smbus.SMBus(1)

def getShort(data, index):
  """Returns two bytes from data as a signed 16-bit value"""
  return c_short((data[index+1] << 8) + data[index]).value

def getUShort(data, index):
  """Returns two bytes from data as an unsigned 16-bit value"""
  return (data[index+1] << 8) + data[index]

# Measuremt configuration
sensor.write_byte_data(ADDRESS, REG_CONTROL, OVERSAMPLE_TEMP<<5 | OVERSAMPLE_PRES<<2 | MODE)

# Read blocks of calibration data from EEPROM
calibrationData = sensor.read_i2c_block_data(ADDRESS, 0x88, 24)

# Convert byte data to word values
digitPlace1 = getUShort(calibrationData, 0)
digitPlace2 = getShort(calibrationData, 2)
digitPlace3 = getShort(calibrationData, 4)

# Wait the required measurement time (see: BMP280 Datasheet 3.8.1)
time.sleep(43.2/1000)

# Read temperature
data = sensor.read_i2c_block_data(ADDRESS, REG_DATA, 8)
rawTemperature = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)

# Refine temperature
value1 = ((((rawTemperature>>3)-(digitPlace1<<1)))*(digitPlace2)) >> 11
value2 = (((((rawTemperature>>4) - (digitPlace1)) * ((rawTemperature>>4) - (digitPlace1))) >> 12) * (digitPlace3)) >> 14
temperature = float((((value1 + value2) * 5) + 128) >> 8) / 100;

print("Temperature: " + str(temperature) + " °C")
