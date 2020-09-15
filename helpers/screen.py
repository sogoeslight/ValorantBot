import pyautogui


def shot(name, x, y, width, height):
    pyautogui.screenshot(region=(x, y, width, height)).save(name)
