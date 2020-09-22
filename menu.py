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


def start_game():
    press_play()
    time.sleep(0.3)
    select_game_mode()
    close_lobby()
    start_search()
    queueing(False)


def play_again():
    skip_stats()
    check_rewards()
    press_play_again()
    queueing(True)


def press_play():
    # click_on('/play.png', 0.95, "Play button pressed",)
    try:
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/play.png', confidence=.85)
    except TypeError:
        time.sleep(1)
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/play.png', confidence=.8)
    # sometimes Play button doesn't presses
    m.click_on_area(x, y, w, h, 10, 5)
    m.click_on_area(x, y, w, h, 10, 5)
    print('Play button pressed')


def select_game_mode():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/deathmatch.png', confidence=.6)
        m.click_on_center(x, y)
        print("Game mode selected")
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/deathmatch.png', confidence=.55)
        m.click_on_center(x, y)
        print("Game mode selected")


def close_lobby():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/close_lobby.png', confidence=.9)
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/close_lobby.png', confidence=.85)
    m.click_on_center(x, y)
    print("Lobby closed")


def start_search():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/small_start.png', confidence=.8)
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/small_start.png', confidence=.85)
    m.click_on_center(x, y)
    print("Searching game...")


def queueing(again):
    thr = threading.Thread(name="queue_timer", target=stats.tick, args=("queue",), daemon=True)
    thr.start()

    if again:
        needed_pic = "/match_found_again.png"
    else:
        needed_pic = "/match_found.png"

    try:
        pos = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                             + '/friends.png', confidence=.85)
        settings.safe_point = pos[0], pos[1]
    except TypeError:
        pass

    m.move_to(settings.safe_point[0], settings.safe_point[1], 0.1)

    # TODO: handle it somehow
    # try:
    #     x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
    #                                           + '/party_restricted.png', confidence=0.7)
    #     while True:
    #         screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
    #         if colors.compare_colors(colors.list_for_party_not_ready,
    #                                  'resources/temp/control_picture_1.png'):
    #             time.sleep(15)
    #             print("Search is restricted")
    #         else:
    #             break
    # except TypeError:
    #     pass

    while True:
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + needed_pic, confidence=.8)
            thr.do_run = False
            thr.join()
            print("Found!")
            break
        except TypeError:
            time.sleep(settings.checks_refresh_rate)

    # check_chat_error()


# TODO: catch error and get this error pic and location
def check_chat_error():
    screen.shot('resources/temp/control_picture_1.png', 290, 1055, 20, 20)
    if colors.compare_colors(colors.list_error_in_chat,
                             'resources/temp/control_picture_1.png'):
        err.handle()


def skip_stats():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/skip.png', confidence=.72)
        m.click_on_center(x, y)
        print("Stats skipped")
    except TypeError:
        try:
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                  + '/skip.png', confidence=.7)
            m.click_on_center(x, y)
            print("Stats skipped")
        except TypeError:
            pass


def check_rewards():
    try:
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/rewards.png', confidence=.75)
        k.press_button('esc')
        print("Rewards acquired")
    except TypeError:
        try:
            time.sleep(1)
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/rewards.png', confidence=.7)
            k.press_button('esc')
            print("Rewards acquired")
        except TypeError:
            pass


def press_play_again():
    x = None
    conf = .7

    while x is None:
        try:
            x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                  + '/play_again.png', confidence=conf)
            m.click_on_center(x, y)
            print('"Play again" pressed', conf)
            break
        except TypeError:
            try:
                x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                      + '/play_again_1.png', confidence=conf)
                m.click_on_center(x, y)
                print('"Play again" pressed', conf)
                break
            except TypeError:
                pass

        conf -= .01
        time.sleep(0.2)


# TODO: regions
def click_on(pic, conf, message, region=None, amount_of_clicks=None, rand_x=None, rand_y=None):
    x = None

    while x is None:
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + pic, confidence=conf)
            m.click_on_center(x, y)
            print(message)
            break
        except TypeError:
            pass

        conf -= .01
        time.sleep(0.2)




















