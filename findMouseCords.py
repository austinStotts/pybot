# run findMouseCords.py to print current mouse position to console

from pynput.mouse import Button, Controller
mouse = Controller()
print(mouse.position)