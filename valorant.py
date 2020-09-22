import cv2
import time
import pyautogui
import settings
from helpers import mouse as m
from helpers import screen, colors


def launch():
    run_command_line('cmd')
    print("Launching Valorant")
    pyautogui.write(settings.valorant_location)
    time.sleep(settings.system_animations_time)
    pyautogui.press('enter')
    exit_command_line()
    time.sleep(settings.average_valorant_load_time)
    # so Valorant window will be focused in case any shit happened
    m.click(settings.safe_point[0], settings.safe_point[1])

    while True:
        # Valorant launched and match continues
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/hundred_hp.png', confidence=.75)

            screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
            if pyautogui.pixelMatchesColor(int(x + w - 3), int(y + h / 2), colors.almost_white, tolerance=4):
                print("\nLaunched successfully into the match\n")
                settings.first_game = False
                settings.was_relaunched_after_error = True
                break
        except TypeError:
            pass

        # Valorant launched and in the main menu
        try:
            x, y, w, h = pyautogui.locateOnScreen('resources/' + settings.resolution_string
                                                  + '/game_launched.png', confidence=.7)
            screen.shot('resources/temp/control_picture_1.png', x, y, w, h)
            if colors.compare_colors(colors.list_for_game_launch,
                                     'resources/temp/control_picture_1.png', tolerance=5):
                print("\nLaunched successfully into the menu\n")
                settings.first_game = True
                break
        except TypeError:
            pass

            print("Waiting for Valorant to launch...")
            time.sleep(settings.checks_refresh_rate + 1)

    settings.valorant_is_opened = True


def kill():
    run_command_line('cmd')
    print("Killing Valorant")
    kill_string = 'taskkill /f /im ' + settings.valorant_process_name
    pyautogui.write(kill_string)
    time.sleep(settings.system_animations_time)
    pyautogui.press('enter')
    exit_command_line()
    settings.valorant_is_opened = False


def run_command_line(command_line):
    print("Opening", command_line)
    pyautogui.hotkey('win', 'r')
    time.sleep(settings.system_animations_time)
    pyautogui.write(command_line)
    pyautogui.press('enter')
    time.sleep(settings.system_animations_time)


def exit_command_line():
    time.sleep(settings.system_animations_time)
    print("Closing command line\n")
    pyautogui.write("exit")
    time.sleep(settings.system_animations_time)
    pyautogui.press('enter')
