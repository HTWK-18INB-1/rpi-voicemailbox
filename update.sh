#!/bin/bash
sudo scripts/upgradeSystem.sh
sudo scripts/loadUpdate.sh
sudo scripts/installDrivers.sh
echo -e "\033[1mAll upgrades finished. Rebooting..\033[0m"
sudo reboot
exit 0
