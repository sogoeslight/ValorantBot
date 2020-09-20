import random
import pyautogui
import settings


def click(x, y):
    movement_time = random.uniform(0.4, 0.75)

    randomize_coordinates(x, y)
    pyautogui.moveTo(x, y, movement_time)

    pyautogui.click(x, y)
    # print("Clicked on " + str(round(new_res_x, 2)) + ", " + str(round(new_res_y, 2)))


def move_to(x, y, speed=None):
    if speed is None:
        movement_time = random.uniform(0.4, 0.7)
    else:
        movement_time = speed

    randomize_coordinates(x, y)
    pyautogui.moveTo(x, y, movement_time)


# Just in case...
def randomize_coordinates(x, y):
    x = random.uniform(x - 5, x + 5)
    y = random.uniform(y - 5, y + 5)
    return x, y
