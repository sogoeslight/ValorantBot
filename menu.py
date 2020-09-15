import time
import settings
import ingame_error as err
from helpers import mouse as m
from helpers import screen, colors


def start_game():
    press_play()
    select_game_mode()
    close_lobby()
    start_search()
    queueing(False)


def play_again():
    skip_stats()
    press_play_again()
    queueing(True)


def press_play():
    m.click(935, 57)
    print('Top "play" button pressed\n')


def select_game_mode():
    m.click(596 + settings.game_mode * 170, 134)
    print("Game mode selected\n")


def close_lobby():
    m.click(805, 235)
    print("Lobby closed\n")


def start_search():
    m.click(935, 1017)
    print("Searching game...\n")


def queueing(again):
    time.sleep(3)

    if again:
        right_color_list = colors.list_for_queing_again
    else:
        right_color_list = colors.list_for_queing

    while True:
        screen.shot('resources/temp/control_picture_1.png', 1875, 1075, 15, 15)
        if colors.compare_colors(right_color_list,
                                 'resources/temp/control_picture_1.png'):
            time.sleep(2)
        else:
            print("Found!\n")
            break

        check_chat_error()


def check_chat_error():
    screen.shot('resources/temp/control_picture_1.png', 290, 1055, 20, 20)
    if colors.compare_colors(colors.list_error_in_chat,
                             'resources/temp/control_picture_1.png'):
        err.handle()


def skip_stats():
    m.click(935, 965)
    print("Stats skipped\n")


def press_play_again():
    m.click(935, 1058)
    print('"Play again" pressed\n')
