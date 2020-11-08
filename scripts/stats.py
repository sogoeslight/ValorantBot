import time
import settings
from colorama import Fore
from datetime import datetime, timedelta

experience_farmed = 0
matches_played = 0

starting_work_time = timedelta()
time_searching = timedelta()
time_in_match = timedelta()
time_handling_errors = timedelta()


def show_current_time():
    print(Fore.CYAN, time.strftime("%H:%M:%S", time.localtime()), Fore.WHITE)


def show():
    print(Fore.WHITE + "\nStatistics:")
    print("   XP farmed:" + Fore.CYAN, matches_played * 900, Fore.WHITE)
    bot_working_time_delta = datetime.now() - timedelta(hours=starting_work_time.hour,
                                                        minutes=starting_work_time.minute,
                                                        seconds=starting_work_time.second)
    print("   Time working:" + Fore.CYAN, bot_working_time_delta.strftime('%H:%M:%S'), Fore.WHITE)
    print("   Time handling errors:" + Fore.CYAN, time_handling_errors, Fore.WHITE)
    if matches_played == 0:
        print("   Average search duration:" + Fore.CYAN, ':'.join(str(time_searching).split(':')[:2]), Fore.WHITE)
        print("   Average match duration:" + Fore.CYAN, ':'.join(str(time_in_match).split(':')[:2]), Fore.WHITE)
    else:
        print("   Average search duration: " + Fore.CYAN,
              ':'.join(str(time_searching / matches_played).split(':')[:2]), Fore.WHITE)
        print("   Average match duration: " + Fore.CYAN,
              ':'.join(str(time_in_match / matches_played).split(':')[:2]), Fore.WHITE)
    print(Fore.WHITE + "Current Time:", end='')
    show_current_time()
