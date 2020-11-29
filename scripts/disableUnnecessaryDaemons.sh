#!/bin/bash
"\033[1mDeactivating unnecessary daemons..\033[0m"
sudo systemctl disable keyboard-setup.service
sudo systemctl disable dphys-swapfile.service
sudo systemctl disable avahi-daemon.service
sudo systemctl disable sys-kernel-debug.mount
sudo systemctl disable raspi-config.service
sudo systemctl disable systemd-udev-trigger.service
sudo systemctl disable rpi-eeprom-update.service
sudo systemctl disable rsyslog.service
sudo systemctl disable systemd-journald.service
sudo systemctl disable systemd-fsck-root.service
sudo systemctl disable systemd-logind.service
sudo systemctl disable bluetooth.service
sudo systemctl disable hciuart.service
exit 0
