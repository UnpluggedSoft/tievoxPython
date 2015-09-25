#!/usr/bin/python    

# Detect off button press and shutdown the system if needed.
# Author: MrLeen

import RPi.GPIO as gpio;
import os;

# Set mode to board numbering.
gpio.setmode(gpio.BOARD);

# Setup pin 7 as input
gpio.setup(7, gpio.IN, pull_up_down=gpio.PUD_DOWN);

if (gpio.input(7) == 0):
  print "[SHUTDOWN] Switch is not set to on. Waiting for on state."
  gpio.wait_for_edge(7, gpio.RISING);
  print "[SHUTDOWN] Switch state set to on. Waiting for off state."

# Reset pin 7 configuration
gpio.cleanup(7);
gpio.setup(7, gpio.IN, pull_up_down=gpio.PUD_DOWN);

# Ensures we have an off button connected first as well
# Setup an interrupt to detect the off button press
gpio.wait_for_edge(7, gpio.FALLING);

# Shutdown
os.system('shutdown -h now');
