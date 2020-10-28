import cv2
import time
import pyautogui
import settings
from colorama import Fore
from helpers import mouse as m
from helpers import screen, colors


def launch():
    run_command_line('cmd')
    print(Fore.YELLOW + "Launching Valorant" + Fore.WHITE)
    pyautogui.write(settings.valorant_location)
    time.sleep(settings.system_animations_time)
    pyautogui.press('enter')
    exit_command_line()
    time.sleep(4)
    check_update()
    time.sleep(settings.average_valorant_load_time)
    # so Valorant window will be focused in case any shit happened
    m.click_on_center(settings.safe_point[0], settings.safe_point[1])

    while True:

        # Valorant launched and match continues
        try:
            x, y, w, h = s.locate_on_screen('/hundred_hp.png', .75)

            screen.shot('../resources/temp/control_picture_1.png', x, y, w, h)
            if pyautogui.pixelMatchesColor(int(x + w - 3), int(y + h / 2), colors.almost_white, tolerance=4):
                print(Fore.GREEN + "\nLaunched successfully into the match\n" + Fore.WHITE)
                settings.first_game = False
                settings.was_relaunched_after_error = True
                break
        except TypeError:
            pass

        # Valorant launched and in the main menu
        try:
            x, y, w, h = s.locate_on_screen('/game_launched.png', .7)
            screen.shot('../resources/temp/control_picture_1.png', x, y, w, h)
            if colors.compare_colors(colors.list_for_game_launch,
                                     '../resources/temp/control_picture_1.png', tolerance=3):
                print(Fore.GREEN + "\nLaunched successfully into the menu\n" + Fore.WHITE)
                settings.first_game = True
                break
        except TypeError:
            pass

            print(Fore.YELLOW + "Waiting for Valorant to launch..." + Fore.WHITE)
            time.sleep(settings.checks_refresh_rate + 1.5)

    settings.valorant_is_opened = True


def check_update():
    try:
        x, y = pyautogui.locateCenterOnScreen('../      resources/' + settings.resolution_string
                                              + '/update_play.png', confidence=.7)
        m.click_on_center(x, y)
        print(Fore.GREEN + "Update window skipped" + Fore.WHITE)
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
