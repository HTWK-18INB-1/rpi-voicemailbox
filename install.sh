#!/bin/bash
sudo scripts/upgradeSystem.sh
sudo scripts/installRequiredPackages.sh
sudo scripts/disableUnnecessaryDaemons.sh
sudo scripts/installDrivers.sh
echo -e "\033[1mInstallation finished. Reboot needed.\033[0m"
exit 0
