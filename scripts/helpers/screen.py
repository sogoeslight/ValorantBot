import pyautogui
import settings


def shot(name, x, y, width, height):
    pyautogui.screenshot(region=(x, y, width, height)).save(name)


def region_maker(x, y, x2, y2):
    return (int(settings.resolution_x * x), int(settings.resolution_y * y),
            int(settings.resolution_x * x2), int(settings.resolution_y * y2))


def locate_center_on_screen(pic, conf, reg=None):
    return pyautogui.locateCenterOnScreen('../resources/' + settings.resolution_string + pic, reg, confidence=conf)


def locate_on_screen(pic, conf, reg=None):
    return pyautogui.locateOnScreen('../resources/' + settings.resolution_string + pic, reg, confidence=conf)
