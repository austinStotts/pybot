import math
import time
from pynput.mouse import Button
from pynput.mouse import Controller as MController
from pynput.keyboard import Key
from pynput.keyboard import Controller as KController

m = MController()
k = KController()

print("going to https://en.wikipedia.org/wiki/Markus_Persson")
print(m.position)

# make a new tab
m.position = (6, 8)
m.click(Button.left, 1)
with k.pressed(Key.ctrl):
  k.press('t')

# select the search bar
m.position = (177, 64)
m.click(Button.left, 1)

# type name of website
k.type('https://en.wikipedia.org/wiki/Markus_Persson')
k.press(Key.enter)