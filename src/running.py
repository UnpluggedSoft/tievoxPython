#!/usr/bin/python

# Blink the running light continuously.
import RPI.GPIO;

gpio.setmode(gpio.BOARD);
gpio.setup(7, gpio.OUT);

while TRUE:
    GPIO.output(7, TRUE);
    time.sleep(5);
    GPIO.output(7, FALSE);
    time.sleep(1);