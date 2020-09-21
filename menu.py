import cv2
import time
import random
import settings
import pyautogui
import ingame_error as err
from datetime import datetime
from helpers import mouse as m
from helpers import screen, colors


def start_game():
    press_play()
    time.sleep(0.3)
    select_game_mode()
    close_lobby()
    start_search()
    queueing()


def play_again():
    skip_stats()
    press_play_again()
    queueing()


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
                                              + '/deathmatch.png', confidence=0.65)
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/deathmatch.png', confidence=0.60)
    m.click(x, y)
    print("Game mode selected")


def close_lobby():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/close_lobby.png', confidence=0.9)
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/close_lobby.png', confidence=0.85)
    m.click(x, y)
    print("Lobby closed")


def start_search():
    try:
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/small_start.png', confidence=0.8)
    except TypeError:
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/small_start.png', confidence=0.85)
    m.click(x, y)
    print("Searching game...")


def queueing():
    try:
        settings.safe_point = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                             + '/friends.png', confidence=0.95)
    except TypeError:
        settings.safe_point = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                             + '/friends.png', confidence=0.8)

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

    try:
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/in_queue.png', confidence=0.55)

        while True:
            screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
            if colors.compare_colors(colors.list_for_party_not_ready,
                                     'resources/temp/control_picture_1.png'):
                print("Found!\n")
                break
            else:
                time.sleep(settings.checks_refresh_rate)
    except TypeError:
        pass

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
                                              + '/skip.png', confidence=0.75)
        m.click(x, y)
    except TypeError:
        try:
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                  + '/skip.png', confidence=0.7)
            m.click(x, y)
        except TypeError:
            pass

    print("Stats skipped")


def press_play_again():
    try:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                              + '/play_again.png', confidence=0.6)
        print("1")
    except TypeError:
        try:
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                  + '/play_again.png', confidence=0.5)
            print("2")
        except TypeError:
            try:
                time.sleep(1)
                x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                      + '/play_again.png', confidence=0.4)
                print("3")
            except TypeError:
                try:
                    time.sleep(1)
                    x, y = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                                          + '/play_again.png', confidence=0.35)
                    print("4")
                except TypeError:
                    print("nope")

    m.click(x, y)
    print('"Play again" pressed')
