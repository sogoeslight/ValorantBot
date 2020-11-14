import cv2
import time
import menu
import stats
import gameplay
import settings
import pyautogui
import ingame_error
from colorama import Fore
from datetime import datetime
from helpers import mouse as m
from helpers import screen, colors


def launch():
    run_command_line('cmd')
    print(Fore.YELLOW + "Launching Valorant" + Fore.WHITE)
    pyautogui.write(settings.valorant_location)
    time.sleep(settings.system_animations_time)
    pyautogui.press('enter')
    exit_command_line()
    time.sleep(10)
    check_update()
    time.sleep(settings.average_valorant_load_time)
    # so Valorant window will be focused in case any shit happened
    m.click_on_center(settings.safe_point[0], settings.safe_point[1])

    while True:
        # Valorant launched into an error
        try:
            x, y, w, h = screen.locate_on_screen('/val51.png', .75)
            m.click_on_area(x, y, w, h)
            time.sleep(settings.average_valorant_closing_time)
            launch()
            break
        except TypeError:
            pass

        print(Fore.YELLOW + "Waiting for Valorant to launch..." + Fore.WHITE)

        # Valorant launched to the match
        try:
            x, y, w, h = screen.locate_on_screen('/hundred_hp.png', .75)
            screen.shot('../resources/temp/control_picture_1.png', x, y, w, h)
            if pyautogui.pixelMatchesColor(int(x + w - 3), int(y + h / 2), colors.almost_white, tolerance=4):
                print(Fore.LIGHTGREEN_EX + "\nLaunched successfully into the match" + Fore.WHITE)
                settings.first_game = False
                settings.was_relaunched_after_error = True
                settings.valorant_is_opened = True
                stats.time_handling_errors += datetime.now() - ingame_error.error_handling_start_time
                if menu.is_in_menu:  # menu -> relaunch -> match
                    gameplay.is_in_match = True
                    gameplay.simulate(False)
                    menu.press_play_again()
                    time.sleep(1)
                    menu.check_rewards()
                else:  # match -> relaunch -> match
                    gameplay.simulate(False)
                break
        except TypeError:
            pass

        # Valorant launched to the main menu
        try:
            x, y, w, h = screen.locate_on_screen('/game_launched.png', .7)
            screen.shot('../resources/temp/control_picture_1.png', x, y, w, h)
            if colors.compare_colors(colors.list_for_game_launch,
                                     '../resources/temp/control_picture_1.png', tolerance=3):
                print(Fore.LIGHTGREEN_EX + "\nLaunched successfully into the menu\n" + Fore.WHITE)
                settings.first_game = True
                settings.valorant_is_opened = True
                stats.time_handling_errors += datetime.now() - ingame_error.error_handling_start_time
                if menu.is_in_menu:  # menu -> relaunch -> menu
                    menu.press_play()
                    time.sleep(.3)
                    menu.select_game_mode()
                    menu.close_lobby()
                    menu.start_search()
                else:  # match -> relaunch -> menu
                    menu.start_game()
                break
        except TypeError:
            pass

        time.sleep(settings.checks_refresh_rate + 1.5)


def check_update():
    try:
        x, y = pyautogui.locateCenterOnScreen('../resources/' + settings.resolution_string
                                              + '/update_play.png', confidence=.7)
        m.click_on_center(x, y)
        print(Fore.LIGHTGREEN_EX + "Update window skipped" + Fore.WHITE)
    except TypeError:
        pass


def kill():
    run_command_line('cmd')
    print(Fore.YELLOW + "Killing Valorant" + Fore.WHITE)
    kill_string = 'taskkill /f /im ' + settings.valorant_process_name
    pyautogui.write(kill_string)
    time.sleep(settings.system_animations_time)
    pyautogui.press('enter')
    exit_command_line()
    settings.valorant_is_opened = False


def run_command_line(command_line):
    print(Fore.YELLOW + "Opening" + Fore.CYAN, command_line, Fore.WHITE)
    pyautogui.hotkey('win', 'r')
    time.sleep(settings.system_animations_time)
    pyautogui.write(command_line)
    pyautogui.press('enter')
    time.sleep(settings.system_animations_time)


def exit_command_line():
    time.sleep(settings.system_animations_time)
    print(Fore.YELLOW + "Closing command line\n" + Fore.WHITE)
    pyautogui.write("exit")
    time.sleep(settings.system_animations_time)
    pyautogui.press('enter')
