#!/bin/bash
./scripts/upgradeSystem.sh
./scripts/loadUpdate.sh
./scripts/installDrivers.sh
echo -e "\033[1mAll upgrades finished. Rebooting..\033[0m"
sudo reboot
exit 0
