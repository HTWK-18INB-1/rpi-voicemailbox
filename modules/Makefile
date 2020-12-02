define MODULE_CONF
# Raspberry Pi voicemailbox drivers\nrpivmb
endef

obj-m += rpivmb.o

all:
	make -j 4 -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

install:
	cp rpivmb.ko /lib/modules/$(shell uname -r)/kernel/drivers/
	echo "$(MODULE_CONF)" > /etc/modules-load.d/rpivmb.conf
	depmod

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
