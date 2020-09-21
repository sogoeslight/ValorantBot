import cv2
import time
import random
import pyautogui
import settings
import ingame_error as err
from helpers import mouse as m
from helpers import keyboard as k
from helpers import screen, colors


def simulate(enable_simulation):
    time.sleep(settings.average_match_load_time + 15)

    # check for in game errors
    try:
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/quit.png', confidence=.8)
        screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
        if colors.compare_colors(colors.list_generic_error,
                                 'resources/temp/control_picture_1.png'):
            print("\nError occurred\n")
            err.handle()
        else:
            buy()
    except TypeError:
        pass

    # Approximately after 45 seconds game counts you as an inactive player
    while True:
        if enable_simulation:
            simulate_movements()
            # simulate_shooting()

        time.sleep(settings.checks_refresh_rate)

        # check for in game errors
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/quit.png', confidence=.8)
            screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
            if colors.compare_colors(colors.list_generic_error,
                                     'resources/temp/control_picture_1.png'):
                print("\nError occurred\n")
                err.handle()
        except TypeError:
            pass

        # check if did not close buy window
        try:
            m.move_to(settings.safe_point[0], settings.safe_point[1], random.uniform(0.1, 0.2))
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/guns/phantom.png', confidence=.85)
            m.move_to(x + random.randint(10, w - 10), y + random.randint(10, h - 10))

            screen.shot('resources/temp/control_picture_1.png', x, y, 30, 30)
            if colors.compare_colors(colors.list_for_hovered_gun_in_buy,
                                     'resources/temp/control_picture_1.png', 5):
                k.press_button('b')
        except TypeError:
            pass

        # check inactivity
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/inactivity.png', confidence=.8)
            screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
            if colors.compare_colors(colors.list_inactivity_message,
                                     'resources/temp/control_picture_1.png'):
                buy()
        except TypeError:
            pass

        # check for end of the match
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/skip.png', confidence=.65)
            screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
            if colors.compare_colors(colors.list_for_match_end, 'resources/temp/control_picture_1.png'):
                print("\nMatch has ended")
                break
        except TypeError:
            pass

        # check for end of the match #2
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/match_end.png', confidence=.8)
            screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
            if colors.compare_colors(colors.list_for_match_end, 'resources/temp/control_picture_1.png'):
                print("\nMatch has ended")
                break
        except TypeError:
            pass


def simulate_movements():
    k.press_button('w', 0.1)


# TODO:
# def simulate_shooting():

def buy():
    k.press_button('b')
    m.move_to(settings.safe_point[0], settings.safe_point[1], random.uniform(0.1, 0.2))
    gun = random.randint(0, 2)
    time.sleep(random.uniform(0.15, 0.25))

    if gun == 0:
        buy_shorty()
    elif gun == 1:
        buy_usp()
    elif gun == 2:
        buy_deagle()
    # print("Bought pistol")
    time.sleep(0.1)

    gun = random.randint(0, 2)
    time.sleep(random.uniform(0.3, 1))

    if gun == 0:
        buy_phantom()
    elif gun == 1:
        buy_vandal()
    elif gun == 2:
        buy_awp()
    # print("Bought gun")
    time.sleep(0.2)

    k.press_button('b')


def buy_phantom():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/phantom.png', confidence=.75)
        m.click(x, y)
    except TypeError:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/phantom.png', confidence=.60)
        m.click(x, y)


def buy_vandal():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/vandal.png', confidence=.75)
        m.click(x, y)
    except TypeError:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/vandal.png', confidence=.60)
        m.click(x, y)


def buy_awp():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/awp.png', confidence=.75)
        m.click(x, y)
    except TypeError:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/awp.png', confidence=.60)
        m.click(x, y)


def buy_shorty():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/shorty.png', confidence=.75)
        m.click(x, y)
    except TypeError:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/shorty.png', confidence=.60)
        m.click(x, y)


def buy_usp():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/usp.png', confidence=.75)
        m.click(x, y)
    except TypeError:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/usp.png', confidence=.60)
        m.click(x, y)


def buy_deagle():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/deagle.png', confidence=.75)
        m.click(x, y)
    except TypeError:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/guns/deagle.png', confidence=.60)
        m.click(x, y)


# TODO:
def buy_first_ability():
    m.click(592, 950)
    # x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
    #                                       + '/.png', confidence=.8)
    # m.click(x, y)


# TODO:
def buy_second_ability():
    m.click(960, 950)
    # x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
    #                                       + '/.png', confidence=.8)
    # m.click(x, y)
