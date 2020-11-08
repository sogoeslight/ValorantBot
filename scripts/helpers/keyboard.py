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


def send_to_chat(msg):
    press_button('enter')

    time.sleep(0.3)
    pyautogui.write('/all ' + msg)
    time.sleep(0.3)

    press_button('enter')
