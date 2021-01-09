import math
import time
from pynput.mouse import Button
from pynput.mouse import Controller as MController
from pynput.keyboard import Key
from pynput.keyboard import Controller as KController
from threading import Timer
from apscheduler.schedulers.blocking import BlockingScheduler

# * * * * * * * * * * * * * * * *
# PLEASE READ
# 
# you will need to install some python packages before this script will work:
# 1. pynput -> use "pip install pynput"
# 2. apscheduler -> use "pip install apscheduler"
#
# once these are installed you can open a commandprompt window
# and navigate into the project folder -> use "cd Desktop/pybot"
# 
# type "python index.py" to run the program
# this program has no means to stop itself and will continue to run untill you close the window
#
# if you wish to change the cordinates for this program you can use "python findMouseCords.py"
# type the command into commandprompt then put your mouse where you want then press enter
#
# * * * * * * * * * * * * * * * * *




# SET THESE VARIABLES BEFORE RUNNING PROGRAM
hours = 2 # time interval
command = "$mk" # what to be typed


def collect_mk():
  print("Collecting Kak...")

  m = MController()
  k = KController()

  # move mouse to message bar & click
  m.position = (-1418, 1339)
  m.click(Button.left, 1)

  # type command and press enter
  k.type(command)
  k.press(Key.enter)

  # move mouse to react location
  m.position = (-1418, 1265)

  # wait for reaction to apear and click
  time.sleep(2)
  m.click(Button.left, 1)

# instantiate scheduler and start the timer
scheduler = BlockingScheduler()
scheduler.add_job(collect_mk, 'interval', minutes=1) # minutes=((hours*60)+1)
print("\nSteve's super duper Kak machine! v1.0.0")
print("will collect Kakera using $mk every " + str(hours) + " hours...")
print("")
collect_mk()
scheduler.start()
