/**
 * RPi button driver
 */
#include <linux/module.h>

MODULE_AUTHOR("Vivien Richter <vivien-richter@outlook.de>");
MODULE_DESCRIPTION("RPi button driver");
MODULE_LICENSE("MIT");
MODULE_VERSION("0.1.0");

int init_module(void) {
	pr_alert("Button ready.\n");
	return 0;
}

void cleanup_module(void) {
	pr_alert("Button end.\n");
}
