#!/usr/bin/python    

# Detect off button press and shutdown the system if needed.
# Author: MrLeen

import RPi.GPIO;
import os;

# Set mode to board numbering.
gpio.setmode(gpi.BOARD);

# Setup pin 11 as input
gpio.setup(11, gpio.IN);

# Ensures we have an off button connected first as well
# Setup an interrupt to detect the off button press
gpio.wait_for_edge(7, gpio.FALLING);

# Shutdown
os.system('shutdown -h now');