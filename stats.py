import time
import settings
import threading

experience_farmed = 0
time_bot_working = 0
time_in_queue = 0
time_in_match = 0
time_handling_errors = 0
games_played = 0


def daemon_timer():
    thr = threading.Thread(name="bot_timer", target=tick, daemon=True)
    thr.start()


def tick(type_of_timer=None):
    global time_bot_working, time_in_match, time_in_queue, time_handling_errors
    thr = threading.currentThread()
    if type_of_timer is None:
        while getattr(thr, "do_run", True):
            time_bot_working += 1
            time.sleep(1)
    elif type_of_timer == "match":
        while getattr(thr, "do_run", True):
            time_in_match += 1
            time.sleep(1)
    elif type_of_timer == "queue":
        while getattr(thr, "do_run", True):
            time_in_queue += 1
            time.sleep(1)
    elif type_of_timer == "error":
        while getattr(thr, "do_run", True):
            time_handling_errors += 1
            time.sleep(1)


def count_game():
    global games_played
    games_played += 1


def show_current_time():
    print("Current Time =", time.strftime("%H:%M:%S", time.localtime()))


def show():
    print("\nStatistics:")
    print("XP farmed:", games_played * 500)
    print("Time working:", time.strftime("%M:%S", time.gmtime(time_bot_working)))
    print("Time handling errors:", time.strftime("%M:%S", time.gmtime(time_handling_errors)))
    if games_played == 0:
        print("Average search duration:",
              time.strftime("%M:%S", time.gmtime(time_in_queue)))
        print("Average match duration:",
              time.strftime("%M:%S", time.gmtime(time_in_match)))
    else:
        print("Average search duration:",
              time.strftime("%M:%S", time.gmtime(time_in_queue / games_played)))
        print("Average match duration:",
              time.strftime("%M:%S", time.gmtime((time_in_match - time_handling_errors -
                                                  settings.average_match_load_time * games_played) / games_played)))
