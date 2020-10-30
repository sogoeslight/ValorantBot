import cv2
import time
import menu
import stats
import random
import settings
import threading
import pyautogui
import ingame_error as err
from colorama import Fore
from helpers import mouse as m
from helpers import screen as s
from helpers import keyboard as k

match_ended = False
stats_thread = None
simulate_buying_thread = None

pistols = ["shorty", "usp", "deagle"]
guns = ["phantom", "vandal", "awp"]


def simulate(enable_simulation):
    global match_ended, simulate_buying_thread, stats_thread
    match_ended = False

    stats_thread = threading.Thread(name="match_timer", target=stats.tick, args=("match",), daemon=True)
    stats_thread.start()

    time.sleep(settings.average_match_load_time + 15)

    simulate_buying_thread = threading.Thread(name="simulation", target=simulate_buying, args=(), daemon=True)
    simulate_buying_thread.start()
    simulate_buying_thread.do_run = True

    k.press_button('b')
    time.sleep(random.uniform(0, .1))
    buy_gun(pistols[random.randint(0, 2)], .85)
    time.sleep(random.uniform(0, .1))
    k.press_button('b')

    # check for in game errors
    try:
        check_for('/quit.png', .9, s.region_maker(.34, .56, .31, .13), "\nError occurred\n", close_threads)
    except TypeError:
        pass

    # Approximately after 45 seconds game counts you as an inactive player
    while True:
        if enable_simulation:
            simulate_movements()
            # simulate_shooting()

        time.sleep(settings.checks_refresh_rate)

        # check for in game errors
        check_for('/quit.png', .9, s.region_maker(.34, .56, .31, .13), "\nError occurred\n", close_threads)

        # check if did not close buy window
        # check_for('/buy.png', .7, s.region_maker(.39, .42, .2, .2), None, k.press_button, 'b')

        # check inactivity
        # check_for('/skip.png', .95, s.region_maker(.39, .255, .22, .12b), None, buy)

        # check for end of the match
        check_for('/skip.png', .7, s.region_maker(.4, .8, .17, .2),
                  "\n" + Fore.CYAN + str(stats.games_played + 1) + Fore.GREEN + ". Match has ended", close_threads)
        if match_ended:
            menu.skip_stats()
            break

        # check for end of the match #2
        check_for('/match_end.png', .9, s.region_maker(.4, .25, .16, .2),
                  "\n" + Fore.CYAN + str(stats.games_played + 1) + Fore.GREEN + ". Match has ended", close_threads)
        if match_ended:
            break


def check_for(pic, conf, region, message=None, func=None, args=None):
    try:
        x, y, w, h = s.locate_on_screen(pic, conf, region)
        if message is not None:
            print(Fore.LIGHTGREEN_EX + message + Fore.WHITE)

        if args is None:
            func()
        else:
            func(*args)
    except TypeError:
        pass


def close_threads():
    global match_ended, simulate_buying_thread, stats_thread
    match_ended = True
    simulate_buying_thread.do_run = False
    simulate_buying_thread.join()
    stats_thread.do_run = False
    stats_thread.join()
    stats.count_game()


def simulate_movements():
    k.press_button('w', .1)


def simulate_buying():
    while getattr(simulate_buying_thread, "do_run", True):
        x = random.randint(25, 35)
        while getattr(simulate_buying_thread, "do_run", True) and x > 0:
            time.sleep(0.2)
            x = x - 0.2
        buy()


# TODO:
# def simulate_shooting():


def buy():
    k.press_button('b')
    time.sleep(random.uniform(0, .2))
    buy_gun(guns[random.randint(0, 2)], .85)
    time.sleep(random.uniform(0, .1))
    k.press_button('b')


def buy_gun(gun, conf):
    while conf > .55:
        try:
            x, y = pyautogui.locateCenterOnScreen('../resources/' + settings.resolution_string
                                                  + '/guns/' + gun + '.png', confidence=conf)
            m.click_on_center(x, y, 0.325)
            break
        except TypeError:
            conf -= .5


# TODO: add ability 1
def buy_first_ability():
    m.click_on_center(592, 950)
    # x, y = pyautogui.locateCenterOnScreen('../resources/' + settings.resolution_string
    #                                       + '/.png', confidence=.8)
    # m.click(x, y)


# TODO: add ability 2
def buy_second_ability():
    m.click_on_center(960, 950)
    # x, y = pyautogui.locateCenterOnScreen('../resources/' + settings.resolution_string
    #                                       + '/.png', confidence=.8)
    # m.click(x, y)
