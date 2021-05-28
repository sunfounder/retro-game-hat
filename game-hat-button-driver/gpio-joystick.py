#!/usr/bin/env python3
import os
os.system("sudo modprobe uinput")
import uinput
import RPi.GPIO as GPIO
import time

DPAD_UP = 5
DPAD_DOWN = 6
DPAD_LEFT = 13
DPAD_RIGHT = 19
A = 26
B = 12
X = 16
Y = 20
TL = 18
TR = 23
START = 21
SELECT = 4

events = (
    uinput.BTN_DPAD_UP,
    uinput.BTN_DPAD_DOWN,
    uinput.BTN_DPAD_LEFT,
    uinput.BTN_DPAD_RIGHT,
    uinput.BTN_A,
    uinput.BTN_B,
    uinput.BTN_X,
    uinput.BTN_Y,
    uinput.BTN_TL,
    uinput.BTN_TR,
    uinput.BTN_TL2,
    uinput.BTN_TR2,
    uinput.BTN_START,
    uinput.BTN_SELECT,
    uinput.ABS_X + (0, 255, 0, 0),
    uinput.ABS_Y + (0, 255, 0, 0),
    uinput.ABS_RX + (0, 255, 0, 0),
    uinput.ABS_RZ + (0, 255, 0, 0),
)
device = uinput.Device(events, name="Retro Game Hat")

# class Test:
#     def emit(self, *a):
#         print(a)
# device = Test()

def create_cb(pin, key):
    def cb(ch):
        if GPIO.input(ch) == 0:
            device.emit(key, 1)
        else:
            device.emit(key, 0)
    return cb

GPIO.setmode(GPIO.BCM)
GPIO.setup(DPAD_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DPAD_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DPAD_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DPAD_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(X, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Y, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(START, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SELECT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

DPAD_UP_cb = create_cb(DPAD_UP, uinput.BTN_DPAD_UP)
DPAD_DOWN_cb = create_cb(DPAD_DOWN, uinput.BTN_DPAD_DOWN)
DPAD_LEFT_cb = create_cb(DPAD_LEFT, uinput.BTN_DPAD_LEFT)
DPAD_RIGHT_cb = create_cb(DPAD_RIGHT, uinput.BTN_DPAD_RIGHT)
A_cb = create_cb(A, uinput.BTN_A)
B_cb = create_cb(B, uinput.BTN_B)
X_cb = create_cb(X, uinput.BTN_X)
Y_cb = create_cb(Y, uinput.BTN_Y)
TL_cb = create_cb(TL, uinput.BTN_TL)
TR_cb = create_cb(TR, uinput.BTN_TR)
START_cb = create_cb(START, uinput.BTN_START)
SELECT_cb = create_cb(SELECT, uinput.BTN_SELECT)

GPIO.add_event_detect(DPAD_UP, GPIO.BOTH, callback=DPAD_UP_cb)
GPIO.add_event_detect(DPAD_DOWN, GPIO.BOTH, callback=DPAD_DOWN_cb)
GPIO.add_event_detect(DPAD_LEFT, GPIO.BOTH, callback=DPAD_LEFT_cb)
GPIO.add_event_detect(DPAD_RIGHT, GPIO.BOTH, callback=DPAD_RIGHT_cb)
GPIO.add_event_detect(A, GPIO.BOTH, callback=A_cb)
GPIO.add_event_detect(B, GPIO.BOTH, callback=B_cb)
GPIO.add_event_detect(X, GPIO.BOTH, callback=X_cb)
GPIO.add_event_detect(Y, GPIO.BOTH, callback=Y_cb)
GPIO.add_event_detect(TL, GPIO.BOTH, callback=TL_cb)
GPIO.add_event_detect(TR, GPIO.BOTH, callback=TR_cb)
GPIO.add_event_detect(START, GPIO.BOTH, callback=START_cb)
GPIO.add_event_detect(SELECT, GPIO.BOTH, callback=SELECT_cb)

while True:
    time.sleep(1)
