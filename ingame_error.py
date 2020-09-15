import time
import valorant
import settings
from helpers import colors, screen


# https://support-valorant.riotgames.com/hc/en-us/articles/360045619633-Error-Codes-in-VALORANT
# 3146 360 750 423 - error window coordinates
def handle():
    valorant.kill()

    for x in range(settings.average_valorant_closing_time, 0, -1):
        time.sleep(1)
        print(x, "second(s) to launch")

    time.sleep(0.5)
    valorant.launch()
