define MODULE_CONF
# Raspberry Pi voicemailbox drivers\nrpi_button
endef

obj-m += rpi_button.o

all:
	make -j 4 -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

install:
	cp rpi_button.ko /lib/modules/$(shell uname -r)/kernel/drivers/
	echo "$(MODULE_CONF)" > /etc/modules-load.d/rpi_button.conf
	depmod

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
