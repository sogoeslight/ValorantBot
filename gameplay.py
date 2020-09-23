import cv2
import time
import stats
import random
import settings
import threading
import pyautogui
import ingame_error as err
from helpers import mouse as m
from helpers import keyboard as k
from helpers import screen, colors


# TODO: regions to every locate
def simulate(enable_simulation):
    thr = threading.Thread(name="match_timer", target=stats.tick, args=("match",), daemon=True)
    thr.start()

    time.sleep(settings.average_match_load_time + 15)

    # check for in game errors
    try:
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/quit.png', confidence=.9)
        print("\nError occurred\n")
        thr.do_run = False
        thr.join()
        err.handle()
    except TypeError:
        buy()

    # Approximately after 45 seconds game counts you as an inactive player
    while True:
        if enable_simulation:
            simulate_movements()
            # simulate_shooting()

        time.sleep(settings.checks_refresh_rate)

        # check for in game errors
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/quit.png', confidence=.9)
            print("\nError occurred\n")
            thr.do_run = False
            thr.join()
            err.handle()
        except TypeError:
            pass

        # check if did not close buy window
        try:
            m.move_to(settings.safe_point[0], settings.safe_point[1], 0.1)
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/guns/phantom.png', confidence=.7)
            m.move_to(x + random.randint(10, w - 10), y + random.randint(10, h - 10))

            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/buy.png', confidence=.7)
            k.press_button('b')
        except TypeError:
            pass

        # check inactivity
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/inactivity.png', confidence=.95)
            buy()
        except TypeError:
            pass

        # check for end of the match
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/skip.png',
                                                  region=(
                                                      int(settings.resolution_x * .4), int(settings.resolution_y * .7),
                                                      int(settings.resolution_x * .17),
                                                      int(settings.resolution_y * .3)),
                                                  confidence=.7)
            print("\nMatch has ended")
            thr.do_run = False
            thr.join()
            stats.count_game()
            break
        except TypeError:
            pass

        # check for end of the match #2
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/match_end.png',
                                                  region=(
                                                      int(settings.resolution_x * 0.4),
                                                      int(settings.resolution_y * 0.25),
                                                      int(settings.resolution_x * 0.17),
                                                      int(settings.resolution_y * 0.2))
                                                  , confidence=.85)
            print("\nMatch has ended")
            thr.do_run = False
            thr.join()
            stats.count_game()
            break
        except TypeError:
            pass


def simulate_movements():
    k.press_button('w', 0.1)


# TODO:
# def simulate_shooting():

def buy():
    pistols = ["shorty", "usp", "deagle"]
    guns = ["phantom", "vandal", "awp"]

    pistol = random.randint(0, 2)
    gun = random.randint(0, 2)

    k.press_button('b')
    m.move_to(settings.safe_point[0], settings.safe_point[1], 0.1)
    time.sleep(0.2)

    buy_gun(pistols[pistol], .85)
    buy_gun(guns[gun], .85)

    time.sleep(0.5)
    k.press_button('b')


def buy_gun(gun, conf):
    while conf > .55:
        try:
            x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                  + '/guns/' + gun + '.png', confidence=conf)
            m.click_on_center(x, y)
            print("Bought", gun, round(conf, 2))
            break
        except TypeError:
            conf -= 0.5

    k.press_button('b')


# TODO: add ability 1
def buy_first_ability():
    m.click_on_center(592, 950)
    # x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
    #                                       + '/.png', confidence=.8)
    # m.click(x, y)


# TODO: add ability 2
def buy_second_ability():
    m.click_on_center(960, 950)
    # x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
    #                                       + '/.png', confidence=.8)
    # m.click(x, y)
