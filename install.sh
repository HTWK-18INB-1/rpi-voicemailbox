#!/bin/bash
echo -e "\033[1mInstalling required packages..\033[0m"
sudo apt update
sudo apt install -y espeak git bc bison flex make libssl-dev libc-dev libncurses-dev raspberrypi-kernel-headers
./upgrade.sh

echo -e "\033[1mInstalling required packages..\033[0m"
cd modules
sudo make install

echo -e "\033[1mInstallation finished.\033[0m"
exit 0
