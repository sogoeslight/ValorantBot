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
    try:
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/play.png', confidence=.85)
    except TypeError:
        time.sleep(1)
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/play.png', confidence=.8)
    # sometimes Play button doesn't presses
    m.click(x + random.uniform(10, w - 10), y + random.uniform(5, h - 5))
    m.click(x + random.uniform(10, w - 10), y + random.uniform(5, h - 5))
    print('Play button pressed')


def select_game_mode():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/deathmatch.png', confidence=.65)
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/deathmatch.png', confidence=.60)
    m.click(x, y)
    print("Game mode selected")


def close_lobby():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/close_lobby.png', confidence=.9)
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/close_lobby.png', confidence=.85)
    m.click(x, y)
    print("Lobby closed")


def start_search():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/small_start.png', confidence=.8)
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/small_start.png', confidence=.85)
    m.click(x, y)
    print("Searching game...")


def queueing(again):
    thr = threading.Thread(name="queue_timer", target=stats.tick, args=("queue",), daemon=True)
    thr.start()

    if again:
        needed_pic = "/match_found_again.png"
    else:
        needed_pic = "/match_found.png"

    try:
        settings.safe_point = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                             + '/friends.png', confidence=.85)
    except TypeError:
        pass

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

    m.move_to(settings.resolution_x * 0.92, settings.resolution_y * 0.1, 0.1)

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
                                              + '/skip.png', confidence=.75)
        m.click(x, y)
        print("Stats skipped")
    except TypeError:
        try:
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                  + '/skip.png', confidence=.7)
            m.click(x, y)
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
    y = None

    while x is None:
        try:
            x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                  + '/play_again.png', confidence=.55)
        except TypeError:
            try:
                x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                      + '/play_again_1.png', confidence=.55)
            except TypeError:
                pass

        time.sleep(0.5)

    m.click(x, y)
    print('"Play again" pressed')
