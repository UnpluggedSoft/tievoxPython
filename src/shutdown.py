#!/usr/bin/python    

# Detect off button press and shutdown the system if needed.
# Author: MrLeen

import RPi.GPIO as gpio;
import os;

def shutdown_callback(channel):
  # Shutdown
  os.system('shutdown -h now');

# Set mode to board numbering.
gpio.setmode(gpio.BOARD);

# Setup pin 7 as input
gpio.setup(7, gpio.IN, pull_up_down=gpio.PUD_DOWN);

if (gpio.input(7) == 0):
  print "[SHUTDOWN] Switch is not set to on. Waiting for on state."
  gpio.wait_for_edge(7, gpio.RISING);

# Reset pin 7 configuration
gpio.cleanup(7);
gpio.setup(7, gpio.IN, pull_up_down=gpio.PUD_DOWN);

# Ensures we have an off button connected first as well
# Setup an interrupt to detect the off button press
gpio.add_event_detect(7, gpio.FALLING);
gpio.add_event_callback(7, shutdown_callback);



