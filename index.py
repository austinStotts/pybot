import math
import time
from pynput.mouse import Button
from pynput.mouse import Controller as MController
from pynput.keyboard import Key
from pynput.keyboard import Controller as KController
from threading import Timer
from apscheduler.schedulers.blocking import BlockingScheduler

m = MController()
k = KController()

hours = 2 # time for kakera claim to reset
command = "$mk" # mudae command to use


def collect_mk():
  print("Collecting Kak...")


  # move mouse to message bar & click
  m.position = (491, 1360)
  m.click(Button.left, 1)

  # type command and press enter
  k.type(command)
  k.press(Key.enter)

  # move mouse to react location
  m.position = (497, 1286)

  # wait for reaction to apear and click
  time.sleep(2)
  m.click(Button.left, 1)




# instantiate scheduler and start the timer
scheduler = BlockingScheduler()
scheduler.add_job(collect_mk, 'interval', minutes=((hours*60)+1))
print("\nSteves super duper Kak machine! v1.0.0")
print("will collect Kakera using $mk in " + str(hours) + " hours...")
scheduler.start()