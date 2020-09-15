import time
import pyautogui
import settings
from helpers import mouse as m
from helpers import screen, colors


def launch():
    run_command_line('cmd')
    print("Launching Valorant")
    pyautogui.write(settings.valorant_location)
    time.sleep(0.8)
    pyautogui.press('enter')
    exit_command_line()
    time.sleep(settings.average_valorant_load_time)
    m.click(1700, 58)  # so Valorant window will be focused in case any shit happened

    while True:
        # Valorant launched and in the main menu
        screen.shot('resources/temp/control_picture_1.png', 1875, 1075, 30, 30)
        if colors.compare_colors(colors.list_for_game_launch,
                                 'resources/temp/control_picture_1.png'):
            print("\nLaunched successfully into the menu\n")
            settings.first_game = True
            break
        else:
            print("Waiting for Valorant to launch...")
            time.sleep(4)

        # Valorant launched and match continues
        if pyautogui.pixel(590, 1052) == colors.just_white:
            print("\nLaunched successfully into the match\n")
            settings.first_game = False
            break

    settings.valorant_is_opened = True


def kill():
    run_command_line('cmd')
    print("Killing Valorant")
    kill_string = 'taskkill /f /im ' + settings.valorant_process_name
    pyautogui.write(kill_string)
    time.sleep(0.8)
    pyautogui.press('enter')
    exit_command_line()
    settings.valorant_is_opened = False


def run_command_line(command_line):
    print("Opening", command_line)
    pyautogui.hotkey('win', 'r')
    time.sleep(0.8)
    pyautogui.write(command_line)
    pyautogui.press('enter')
    time.sleep(0.8)


def exit_command_line():
    print("Closing command line\n")
    pyautogui.write("exit")
    time.sleep(0.8)
    pyautogui.press('enter')
