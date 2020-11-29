#!/bin/bash
./scripts/upgradeSystem.sh
./scripts/installRequiredPackages.sh
./scripts/disableUnnecessaryDaemons.sh
./scripts/installDrivers.sh
echo -e "\033[1mInstallation finished. Reboot needed.\033[0m"
exit 0
