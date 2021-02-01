/**
 * RPi button driver
 */
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/cdev.h>

MODULE_DESCRIPTION("RPi button driver");
MODULE_AUTHOR("Vivien Richter <vivien-richter@outlook.de>");
MODULE_LICENSE("Dual MIT/GPL");
MODULE_VERSION("0.2.1");

// Configuration
#define GPIO_BUTTON 16
#define DEVICE_NAME "button"

/**
 * Defines custom printk messages
 */
#undef pr_fmt
#define pr_fmt(fmt) KBUILD_MODNAME ": " fmt

/**
 * Holds the MAJOR and MINOR numbers of the device inode
 */
static dev_t device;

/**
 * Character device class pointer
 */
static struct class *cdevcp;

/**
 * Character device structure
 */
static struct cdev cdevs;

/**
 * Opens the device
 */
static int device_open(struct inode *inode, struct file  *fp) {
	return 0;
}

/**
 * Reads from the device
 */
static ssize_t device_read(struct file *fp, char *buffer, size_t length, loff_t *offset) {
	return 0;
}

/**
 * Releases the device
 */
static int device_close(struct inode *inode, struct file *fp) {
	return 0;
}

// Registers character device handlers
static struct file_operations fops = {
	.owner = THIS_MODULE,
	.open = device_open,
	.read = device_read,
	.release = device_close
};

/**
 * Driver initialization
 */
int init_module(void) {
	int allocChrDevRegionResult = alloc_chrdev_region(&device, 0, 1, KBUILD_MODNAME);
	if(allocChrDevRegionResult < 0) {
        pr_err("alloc_chrdev_region returned: %d\n", allocChrDevRegionResult);
        return -1;
    } else {
		pr_debug("Character device region allocated, MAJOR: %d, MINOR: %d.\n", MAJOR(device), MINOR(device));
		// Create the character device class
		if ((cdevcp = class_create(THIS_MODULE, KBUILD_MODNAME)) == NULL) {
			unregister_chrdev_region(device, 1);
			pr_err("class_create failed.\n");
			return -1;
		} else {
			pr_debug("Character device class created.\n");
			// Create the character device
			if (device_create(cdevcp, NULL, device, NULL, DEVICE_NAME) == NULL) {
				class_destroy(cdevcp);
				unregister_chrdev_region(device, 1);
				pr_err("device_create failed.\n");
				return -1;
			} else {
				pr_debug("Character device created.\n");
				// Initialize character device
				cdev_init(&cdevs, &fops);
				pr_debug("Character device initialized.\n");
				// Add the character device to the system
				int addChrDevResult = cdev_add(&cdevs, device, 1);
				if (addChrDevResult < 0) {
					device_destroy(cdevcp, device);
			    	class_destroy(cdevcp);
			    	unregister_chrdev_region(device, 1);
					pr_err("cdev_add returned: %d\n", addChrDevResult);
					return -1;
				} else {
					pr_info("Registered as /dev/%s\n", DEVICE_NAME);
					// Ready
					return 0;
				}
			}
		}
	}
}

/**
 * Driver destructor
 */
void cleanup_module(void) {
	cdev_del(&cdevs);
	device_destroy(cdevcp, device);
	class_destroy(cdevcp);
	unregister_chrdev_region(device, 1);
	pr_info("Unloaded.\n");
	return;
}
