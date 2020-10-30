import time
import stats
import settings
import threading
import ingame_error as err
from colorama import Fore
from helpers import colors
from helpers import mouse as m
from helpers import keyboard as k
from helpers import screen as s, colors


def start_game():
    press_play()
    time.sleep(.3)
    select_game_mode()
    close_lobby()
    start_search()
    queueing(False)


def play_again():
    check_rewards()
    # skip_stats()  # TODO: recheck?
    press_play_again()
    queueing(True)


def press_play():
    find_and_click_on('/play.png', .9, s.region_maker(.4, .02, .17, .05), "Play button pressed", None,
                      amount_of_clicks=2)


def select_game_mode():
    find_and_click_on('/deathmatch.png', .75, s.region_maker(.51, .08, .125, .05), "Game mode selected",
                      '/deathmatch_1.png')


def close_lobby():
    find_and_click_on('/close_lobby.png', .85, s.region_maker(.345, .155, .16, .09), "Lobby closed",
                      '/close_lobby_1.png')


def start_search():
    find_and_click_on('/small_start.png', .8, s.region_maker(.38, .835, .22, .13), "Searching game...")


def queueing(again):
    thr = threading.Thread(name="queue_timer", target=stats.tick, args=("queue",), daemon=True)
    thr.start()

    try:
        pos = s.locate_center_on_screen('/friends.png', .85)
        settings.safe_point = pos[0], pos[1]
    except TypeError:
        pass

    m.move_to(settings.safe_point[0], settings.safe_point[1], .1)

    if again:
        needed_pic = "/match_found_again.png"
    else:
        needed_pic = "/match_found.png"

    while True:
        try:
            x, y, w, h = s.locate_on_screen(needed_pic, .8)
            thr.do_run = False
            thr.join()
            print(Fore.LIGHTGREEN_EX + "Found!" + Fore.WHITE)
            break
        except TypeError:
            time.sleep(settings.checks_refresh_rate)

    # check_chat_error()


# TODO: catch error and get this error pic and location
def check_chat_error():
    screen.shot('../resources/temp/control_picture_1.png', 290, 1055, 20, 20)
    if colors.compare_colors(colors.list_error_in_chat,
                             '../resources/temp/control_picture_1.png'):
        err.handle()


def skip_stats():
    find_and_click_on('/skip.png', .8, s.region_maker(.41, .81, .15, .1), "Stats skipped")


# TODO: double check - when they take place, add region
def check_rewards():
    try:
        x, y, w, h = s.locate_on_screen('/rewards.png', .75)
        k.press_button('esc')
        print(Fore.LIGHTGREEN_EX + "Rewards acquired" + Fore.WHITE)
    except TypeError:
        try:
            x, y, w, h = s.locate_on_screen('/rewards.png', .7)
            k.press_button('esc')
            print(Fore.LIGHTGREEN_EX + "Rewards acquired" + Fore.WHITE)
        except TypeError:
            pass


def press_play_again():
    m.click_on_center(settings.resolution_x / 2, settings.resolution_y * .935)
    print(Fore.LIGHTGREEN_EX + '"Play again" pressed' + Fore.WHITE)
    # region = s.region_maker(.35, .85, .27, .15)
    # pyautogui.screenshot(region=region).save("../resources/press_play_again.png")
    # find_and_click_on('/play_again.png', 0.99, '"Play again" pressed', region, '/play_again_1.png', 0.1)


def find_and_click_on(pic, conf, region, message=None, second_pic=None, speed=None, amount_of_clicks=None, delay=None):
    x = None
    while (x is None) & (conf > .6):
        try:
            click_on(pic, conf, message, region, speed, amount_of_clicks)
            break
        except TypeError:
            if second_pic is not None:
                try:
                    click_on(second_pic, conf, message, region, speed, amount_of_clicks)
                except TypeError:
                    pass

        if delay is not None:
            time.sleep(delay)
        print(Fore.RED + str(conf) + Fore.WHITE)
        conf -= .03


def click_on(pic, confidence, message, region, speed=None, amount_of_clicks=None):
    x, y, w, h = s.locate_on_screen(pic, confidence, region)

    if amount_of_clicks is None:
        m.click_on_area(x, y, w, h, speed)
    else:
        for i in range(amount_of_clicks):
            m.click_on_area(x, y, w, h, speed)

    print(Fore.LIGHTGREEN_EX + message + Fore.WHITE)


    # TODO: handle it in queue somehow
    # try:
    #     x, y, w, h = s.locate_on_screen('/party_restricted.png', .7)
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
