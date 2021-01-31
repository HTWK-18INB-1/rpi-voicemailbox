#!/usr/bin/python3

import time
import struct
import wave
from smbus import SMBus

# Settings
bus = 1
address = 0x48
duration = 10 # seconds
filename = "test.wav"

# Prepare
file = wave.open(filename, 'w')
file.setnchannels(1) # Mono
file.setframerate(860) # Frames per second
file.setsampwidth(2) # 2 bytes per frame
adc = SMBus(bus)

# Reset
adc.write_byte(0x00, 0x06)
time.sleep(0.5)

# Set configuration
# 1 101 111 0 = de
# 111 0 1 0 00 = e8
adc.write_i2c_block_data(address, 0x01, [0xde, 0xe8])
time.sleep(0.5)

# Record input
for frame in range(int(duration * 860)):
    data = adc.read_i2c_block_data(address, 0x00, 2)
    value = data[0] * 256 + data[1]
    if value > 32767: value -= 65535
    print(value)
    file.writeframesraw(struct.pack("<h", value))
    time.sleep(1/860)
