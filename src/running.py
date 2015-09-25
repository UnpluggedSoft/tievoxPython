#!/usr/bin/python

# Blink the running light continuously.
import RPi.GPIO as gpio;
import time;

gpio.setwarnings(False);
gpio.setmode(gpio.BOARD);
gpio.setup(7, gpio.OUT);

while True:
    gpio.output(7, True);
    time.sleep(5);
    gpio.output(7, False);
    time.sleep(1);