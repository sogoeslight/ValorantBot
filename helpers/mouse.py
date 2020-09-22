import random
import pyautogui
import settings


def click_on_center(x, y):
    movement_time = random.uniform(0.4, 0.75)

    randomize_move(x, y)
    pyautogui.moveTo(x, y, movement_time)

    pyautogui.click(x, y)
    # print("Clicked on " + str(round(new_res_x, 2)) + ", " + str(round(new_res_y, 2)))


def click_on_area(x, y, w, h, rand_x=5, rand_y=2):
    movement_time = random.uniform(0.4, 0.75)

    x, y = randomize_click(x, y, w, h, rand_x, rand_y)

    pyautogui.moveTo(x, y, movement_time)
    pyautogui.click(x, y)


def move_to(x, y, speed=None):
    if speed is None:
        movement_time = random.uniform(0.4, 0.7)
    else:
        movement_time = speed + random.uniform(0.05, 0.1)

    x, y = randomize_move(x, y)
    pyautogui.moveTo(x, y, movement_time)


# Just in case...
def randomize_move(x, y):
    x = random.uniform(x - 5, x + 5)
    y = random.uniform(y - 5, y + 5)
    return x, y


def randomize_click(x, y, w, h, rand_x, rand_y):
    x += random.uniform(rand_x, w - rand_x)
    y += random.uniform(rand_y, h - rand_y)
    return x, y
