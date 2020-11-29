obj-m += rpivmb.o

all:
	make -j 4 -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules

install:
	ln -sf rpivmb.ko /lib/modules/$(shell uname -r)/kernel/drivers/rpivmb.ko
	grep -qxF "rpivmb" /etc/modules || echo "rpivmb" >> /etc/modules

clean:
	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
