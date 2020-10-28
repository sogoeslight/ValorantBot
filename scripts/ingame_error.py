import time
import stats
import valorant
import settings
import threading
from colorama import Fore
from helpers import colors, screen


# https://support-valorant.riotgames.com/hc/en-us/articles/360045619633-Error-Codes-in-VALORANT
# 3146 360 750 423 - error window coordinates
def handle():
    thr = threading.Thread(name="error", target=stats.tick, args=("error",), daemon=True)
    thr.start()

    valorant.kill()

    for x in range(settings.average_valorant_closing_time, 0, -1):
        time.sleep(1)
        print(Fore.CYAN, x, Fore.YELLOW + "second(s) to launch")

    time.sleep(.5)
    valorant.launch()

    thr.do_run = False
    thr.join()
