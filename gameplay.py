import time
import random
import pyautogui
import settings
import ingame_error as err
from helpers import mouse as m
from helpers import keyboard as k
from helpers import screen, colors


def simulate(enable_simulation):
    time.sleep(settings.average_match_load_time + 20)

    # check for in game errors
    screen.shot('resources/temp/control_picture_1.png', 841, 653, 20, 20)
    if colors.compare_colors(colors.list_generic_error,
                             'resources/temp/control_picture_1.png'):
        print("\nError occurred\n")
        err.handle()
    else:
        buy()

    # Approximately after 45 seconds game counts you as an inactive player
    while True:
        if enable_simulation:
            simulate_movements()
            # simulate_shooting()

        time.sleep(4)

        # check for in game errors
        screen.shot('resources/temp/control_picture_1.png', 841, 653, 20, 20)
        if colors.compare_colors(colors.list_generic_error,
                                 'resources/temp/control_picture_1.png'):
            print("\nError occurred\n")
            err.handle()

        # check if did not close buy window
        m.move_to(920, 580)
        screen.shot('resources/temp/control_picture_1.png', 810, 515, 20, 20)
        if colors.compare_colors(colors.list_for_hovered_gun_in_buy,
                                 'resources/temp/control_picture_1.png'):
            k.press_button('b')

        # check inactivity
        screen.shot('resources/temp/control_picture_1.png', 805, 370, 20, 20)
        if colors.compare_colors(colors.list_inactivity_message,
                                 'resources/temp/control_picture_1.png'):
            buy()

        # check for end of the match
        screen.shot('resources/temp/control_picture_1.png', 919, 398, 30, 30)
        if (colors.compare_colors(colors.list_for_match_end,
                                  'resources/temp/control_picture_1.png')
                | bool(pyautogui.pixel(938, 123) == colors.just_white)):
            print("\nMatch has ended")
            break


def simulate_movements():
    k.press_button('w', 0.1)


# TODO:
# def simulate_shooting():

def buy():
    k.press_button('b')
    gun = random.randint(0, 2)
    time.sleep(random.uniform(0.5, 0.8))

    if gun == 0:
        buy_shorty()
    elif gun == 1:
        buy_usp()
    elif gun == 2:
        buy_deagle()
    print("Bought pistol")
    time.sleep(0.3)

    gun = random.randint(0, 2)
    time.sleep(random.uniform(0.3, 1))

    if gun == 0:
        buy_phantom()
    elif gun == 1:
        buy_vandal()
    elif gun == 2:
        buy_awp()
    print("Bought gun")
    time.sleep(0.5)

    k.press_button('b')


def buy_phantom():
    m.click(914, 575)


def buy_vandal():
    m.click(914, 730)


def buy_awp():
    m.click(1194, 420)


def buy_shorty():
    m.click(480, 380)


def buy_usp():
    m.click(480, 620)


def buy_deagle():
    m.click(480, 740)


def buy_first_ability():
    m.click(592, 950)


def buy_second_ability():
    m.click(960, 950)
