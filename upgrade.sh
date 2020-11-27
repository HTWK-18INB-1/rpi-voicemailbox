#!/bin/bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt autoremove --purge -y
sudo apt install -fy
sudo rpi-eeprom-update -a
exit 0
