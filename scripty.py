import random
import time
import keyboard
import pyautogui
import win32api
import win32con
from pynput.keyboard import Controller, Key
from coordinateRead import read_coords

keyboard1 = Controller()


# 90 DEGREE ANGLE, LOOK AT 18.3

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard1.type(character)  # Type the character
        delay = random.uniform(0, 2)  # Generate a random number between 0 and 10
        time.sleep(delay)
    keyboard1.press(Key.enter)
    time.sleep(0.5)
    keyboard1.release(Key.enter)


def redo_farm():
    if pyautogui.locateOnScreen("reconnect.PNG"):
        x, y = pyautogui.locateCenterOnScreen("reconnect.PNG")
        click(x, y)
        time.sleep(15)
        type_string_with_delay("/play sb")
        time.sleep(5)
        type_string_with_delay("/warp home")
        start_farm()
    elif pyautogui.locateOnScreen("hub.png", grayscale=True, confidence=0.6):
        type_string_with_delay("/warp home")
        start_farm()


def start_farm():
    while read_coords()[2] != 78:
        pyautogui.mouseDown()
        keyboard1.press("a")
    time.sleep(1)
    keyboard1.release("a")
    print("next layer")
    while read_coords()[2] != -77:
        keyboard1.press("w")
    time.sleep(1)
    keyboard1.release("w")
    print("next layer")


time.sleep(4)
while True:
    for i in range(5):
        start_farm()
    pyautogui.mouseDown()
    time.sleep(random.randint(0, 5))
