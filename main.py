# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       student                                                      #
# 	Created:      5/19/2025, 3:04:37 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
import math

# Brain should be defined by default
brain = Brain()
controller = Controller()
wheel = Motor(Ports.PORT1)
leftStickY = 0
leftStickRelative = 0

def update():
    global leftStickY
    global leftStickRelative

    leftStickY = controller.axis3.position()
    leftStickRelative = math.sin(math.pi/200 * leftStickY) * 100

def logAxis(): 
    brain.screen.print(leftStickRelative)

controller.buttonA.pressed(logAxis)

def drive(direction):
    if direction == FORWARD:
        wheel.spin(direction, leftStickRelative)
    else:
        wheel.spin(direction, leftStickRelative * -1)



while True:
    update()

    if leftStickY > 0:
        drive(FORWARD)
    elif leftStickY < 0:
        drive(REVERSE)
    else:
        wheel.stop()