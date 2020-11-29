#!/bin/bash
echo -e "\033[1mUpgrading system packages..\033[0m"
sudo apt update && sudo apt dist-upgrade -y
sudo apt autoremove --purge -y
sudo apt install -fy
sudo rpi-eeprom-update -a
exit 0
