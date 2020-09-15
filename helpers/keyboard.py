import time
import pyautogui


def press_button(key, time_in_seconds=None):
    if time_in_seconds is not None:
        pyautogui.keyDown(key)
        time.sleep(time_in_seconds)
        pyautogui.keyUp(key)
    else:
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
