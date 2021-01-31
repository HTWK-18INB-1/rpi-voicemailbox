#!/usr/bin/python

import os
text = "Hallo World!"
volume = 200
speed = 150
voice = "en+f5"
os.system("espeak -a " + str(volume) + " -s " + str(speed) + " -v " + voice + " '" + text + "' --stdout | aplay 2> /dev/null")
