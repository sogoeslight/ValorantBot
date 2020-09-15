import random
import pyautogui
import settings


def click(x, y):
    movement_time = random.uniform(0.6, 1.2)
    # Just in case...
    x = random.randint(x - 5, x + 5)
    y = random.randint(y - 5, y + 5)

    pyautogui.moveTo(x, y, movement_time)
    new_res_x = x / 1920 * settings.resolution_x
    new_res_y = (y - 31) / 1080 * settings.resolution_y + settings.border

    pyautogui.click(new_res_x, new_res_y)
    print("Clicked on " + str(round(new_res_x, 2)) + ", " + str(round(new_res_y, 2)))


def move_to(x, y):
    x = random.randint(x - 3, x + 3)
    y = random.randint(y - 3, y - 3)

    pyautogui.moveTo(x, y)
