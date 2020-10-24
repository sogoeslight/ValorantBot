import time
import stats
import settings
import threading
import pyautogui
import ingame_error as err
from helpers import mouse as m
from helpers import keyboard as k
from helpers import screen, colors


def start_game():
    press_play()
    time.sleep(.3)
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
    region = (settings.resolution_x * .40, settings.resolution_y * .02,
              settings.resolution_x * .17, settings.resolution_y * .05)
    find_and_click_on('/play.png', 0.9, "Play button pressed", region, None, 2)



def select_game_mode():
    # region = (settings.resolution_x * .24, settings.resolution_y * .06,
    #          settings.resolution_x * .5, settings.resolution_y * .12)
    region = (settings.resolution_x * .51, settings.resolution_y * .08,
              settings.resolution_x * .125, settings.resolution_y * .05)
    find_and_click_on('/deathmatch.png', 0.75, "Game mode selected", region, '/deathmatch_1.png')


def close_lobby():
    region = (settings.resolution_x * .345, settings.resolution_y * .155,
              settings.resolution_x * .16, settings.resolution_y * .09)
    find_and_click_on('/close_lobby.png', 0.95, "Lobby closed", region, '/close_lobby_1.png')


def start_search():
    region = (settings.resolution_x * .38, settings.resolution_y * .835,
              settings.resolution_x * .22, settings.resolution_y * .13)
    find_and_click_on('/small_start.png', 0.9, "Searching game...", region)


def queueing(again):
    thr = threading.Thread(name="queue_timer", target=stats.tick, args=("queue",), daemon=True)
    thr.start()

    try:
        pos = pyautogui.locateCenterOnScreen('resources/' + settings.resolution_string
                                             + '/friends.png', confidence=.85)
        settings.safe_point = pos[0], pos[1]
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
    region = (settings.resolution_x * .41, settings.resolution_y * .81,
              settings.resolution_x * .15, settings.resolution_y * .1)
    find_and_click_on('/skip.png', 0.9, "Stats skipped", region)


# TODO: double check - when they take place, add region
def check_rewards():
    try:
        x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                              + '/rewards.png', confidence=.75)
        k.press_button('esc')
        print("Rewards acquired")
    except TypeError:
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/rewards.png', confidence=.7)
            k.press_button('esc')
            print("Rewards acquired")
        except TypeError:
            pass


def press_play_again():
    m.click_on_center(settings.resolution_x / 2, settings.resolution_y * .935)
    print('"Play again" pressed')
    # region = (settings.resolution_x * .35, settings.resolution_y * .85,
    #           settings.resolution_x * .27, settings.resolution_y * .15)
    # pyautogui.screenshot(region=region).save("resources/press_play_again.png")
    # find_and_click_on('/play_again.png', 0.99, '"Play again" pressed', region, '/play_again_1.png', 0.1)


def find_and_click_on(pic, conf, message, region, second_pic=None, amount_of_clicks=None, delay=None):
    x = None
    while (x is None) & (conf > .5):
        try:
            click_on(pic, conf, message, region, amount_of_clicks)
            break
        except TypeError:
            if second_pic is not None:
                try:
                    click_on(second_pic, conf, message, region, amount_of_clicks)
                except TypeError:
                    pass

        if delay is not None:
            time.sleep(delay)
        print(conf)
        conf -= .03


def click_on(pic, conf, message, region, amount_of_clicks=None):
    x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                          + pic, region, confidence=conf)

    if amount_of_clicks is None:
        m.click_on_area(x, y, w, h)
    else:
        for i in range(amount_of_clicks):
            m.click_on_area(x, y, w, h)

    print(message)



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
