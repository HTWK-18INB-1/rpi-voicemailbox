#!/usr/bin/python

import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

# Configure as output
spi.xfer([0x40, 0x00, 0x00])
spi.xfer([0x40, 0x01, 0x00])

# Set digit
spi.xfer([0x40, 0x14, 0x00])

while True:
    # On
    spi.xfer([0x40, 0x15, 0x08])
    # wait 2s
    time.sleep(2)
    # Off
    spi.xfer([0x40, 0x15, 0x00])
    # wait 2s
    time.sleep(2)
