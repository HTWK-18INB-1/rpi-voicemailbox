#!/bin/bash
echo -e "\033[1mUpgrading packages..\033[0m"
sudo apt update && sudo apt dist-upgrade -y
sudo apt autoremove --purge -y
sudo apt install -fy
sudo rpi-eeprom-update -a

echo -e "\033[1mLoading application updates..\033[0m"
git pull origin master

echo -e "\033[1mBuilding driver..\033[0m"
cd modules
make

echo -e "\033[1mAll upgrades finished.\033[0m"
exit 0
