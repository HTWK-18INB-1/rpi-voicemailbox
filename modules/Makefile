obj-m += rpivmb.o

all:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

install:
	ln -s rpivmb.ko /lib/modules/$(shell uname -r)/kernel/drivers/rpivmb.ko
	grep -qxF "rpivmb" /etc/modules || echo "rpivmb" >> /etc/modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
