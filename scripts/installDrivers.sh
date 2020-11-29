#!/bin/bash
echo -e "\033[1mBuilding drivers..\033[0m"
cd modules
make
make install
exit 0
