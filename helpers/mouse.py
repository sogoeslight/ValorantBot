import random
import pyautogui
import settings


def click_on_center(x, y):
    movement_time = random.uniform(.4, .75)
    x, y = randomize_center_coordinates(x, y)
    pyautogui.moveTo(x, y, movement_time)
    pyautogui.click(x, y)
    # print("Clicked on " + str(round(x, 2)) + ", " + str(round(y, 2)))


def move_to(x, y, speed=None):
    if speed is None:
        movement_time = random.uniform(.4, .7)
    else:
        movement_time = speed + random.uniform(.05, .1)

    pyautogui.moveTo(x, y, movement_time)


def randomize_center_coordinates(x, y, low_plank=5, high_plank=5):
    x = random.uniform(x - low_plank, x + high_plank)
    y = random.uniform(y - low_plank, y + high_plank)
    return x, y


def click_on_area(x, y, w, h):
    movement_time = random.uniform(.4, .75)
    x, y = randomize_area_coordinates(x, y, w, h)
    pyautogui.moveTo(x, y, movement_time)
    pyautogui.click(x, y)


def randomize_area_coordinates(x, y, w, h, low_plank=.3, high_plank=.7):
    x += random.uniform(w * low_plank, w * high_plank)
    y += random.uniform(h * low_plank, h * high_plank)
    return x, y
