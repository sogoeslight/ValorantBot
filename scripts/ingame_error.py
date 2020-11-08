import time
import stats
import valorant
import settings
import gameplay
import threading
from colorama import Fore
from datetime import datetime
from helpers import colors, screen

error_checker_thread = None
error_handling_start_time = None


# https://support-valorant.riotgames.com/hc/en-us/articles/360045619633-Error-Codes-in-VALORANT
# 3146 360 750 423 - error window coordinates
def checker_thread():
    global error_checker_thread
    error_checker_thread = threading.Thread(name="error_checker", target=check, daemon=True)
    error_checker_thread.daemon = True
    error_checker_thread.start()


def check():
    while getattr(error_checker_thread, "do_run", True):
        time.sleep(5)
        try:
            gameplay.check_for('/quit.png', .7, screen.region_maker(.34, .56, .31, .13),
                               Fore.YELLOW + "\nError occurred\n", handle)
        except TypeError:
            pass


def close_thread():
    global error_checker_thread
    error_checker_thread.do_run = False


def handle():
    global error_handling_start_time

    if gameplay.is_in_match:
        gameplay.close_threads()

    error_handling_start_time = datetime.now()

    valorant.kill()

    for x in range(settings.average_valorant_closing_time, 0, -1):
        time.sleep(1)
        if x == 1:
            print(" ", Fore.CYAN, x, Fore.YELLOW + "second to launch\n")
        else:
            print(" ", Fore.CYAN, x, Fore.YELLOW + "seconds to launch")

    time.sleep(.5)
    valorant.launch()
