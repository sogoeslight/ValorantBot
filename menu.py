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
    region = (settings.resolution_x * .3, 0,
              settings.resolution_x * .37, settings.resolution_y * .2)
    pyautogui.screenshot(region=region).save("resources/press_play.png")
    find_and_click_on('/play.png', 0.95, "Play button pressed", region, None, 2)


def select_game_mode():
    region = (settings.resolution_x * .23, settings.resolution_y * .05,
              settings.resolution_x * .51, settings.resolution_y * .15)
    pyautogui.screenshot(region=region).save("resources/select_game_mode.png")
    find_and_click_on('/deathmatch.png', 0.75, "Game mode selected", region)


def close_lobby():
    region = (settings.resolution_x * .3, settings.resolution_y * .1,
              settings.resolution_x * .37, settings.resolution_y * .2)
    pyautogui.screenshot(region=region).save("resources/close_lobby.png")
    find_and_click_on('/close_lobby.png', 0.95, "Lobby closed", region)


def start_search():
    region = (settings.resolution_x * .35, settings.resolution_y * .8,
              settings.resolution_x * .27, settings.resolution_y * .2)
    pyautogui.screenshot(region=region).save("resources/start_search.png")
    find_and_click_on('/small_start.png', 0.9, "Searching game...", region)


def queueing(again):
    thr = threading.Thread(name="queue_timer", target=stats.tick, args=("queue",), daemon=True)
    thr.start()

    # TODO: vinesti
    try:
        pos = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                             + '/friends.png', confidence=.85)
        settings.safe_point = pos
    except TypeError:
        pass

    m.move_to(settings.safe_point[0], settings.safe_point[1], 0.1)

    if again:
        needed_pic = "/match_found_again.png"
    else:
        needed_pic = "/match_found.png"

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
    region = (settings.resolution_x * .4, settings.resolution_y * .7,
              settings.resolution_x * .17, settings.resolution_y * .3)
    pyautogui.screenshot(region=region).save("resources/skip_stats.png")
    find_and_click_on('/skip.png', 0.9, "Stats skipped", region)


# TODO: double check - when they take place
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
    region = (settings.resolution_x * .35, settings.resolution_y * .85,
              settings.resolution_x * .27, settings.resolution_y * .15)
    pyautogui.screenshot(region=region).save("resources/press_play_again.png")
    find_and_click_on('/play_again.png', 0.99, '"Play again" pressed', region, '/play_again_1.png')


def find_and_click_on(pic, conf, message, region, second_pic=None, amount_of_clicks=None):
    x = None
    while x is None:
        try:
            if conf < .4:
                break
            click_on(pic, conf, message, region, amount_of_clicks)
            break
        except TypeError:
            if second_pic is None:
                pass
            else:
                try:
                    click_on(second_pic, conf, message, region, amount_of_clicks)
                except TypeError:
                    pass

        conf -= .01


def click_on(pic, conf, message, region, amount_of_clicks=None):
    x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                          + pic, region, confidence=conf)

    if amount_of_clicks is None:
        m.click_on_area(x, y, w, h)
    else:
        for i in range(amount_of_clicks):
            m.click_on_area(x, y, w, h)

    print(message, conf)



    # TODO: handle it in queue somehow
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
