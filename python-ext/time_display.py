import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637

# GPIO23 -- CLK 
# GPIO24 -- DI0 

# new module
time_display = tm1637.TM1637(23,24)
# from 0 to 7
time_display.brightness(0) 

while(True):
    # get current time
    now = datetime.datetime.now()
    # store time as [String]
    currenttime = f"{int(now.hour / 10)}{now.hour % 10}{int(now.minute / 10)}{now.minute % 10}"
    # display the time
    time_display.show(currenttime)
    # re-check every second
    time.sleep(1)