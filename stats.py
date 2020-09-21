import time
import threading

experience_farmed = 0
time_bot_working = 0
time_in_queue = 0
time_in_match = 0
error_handling_time = 0
games_played = 0


def daemon_timer():
    thr = threading.Thread(name="bot_timer", target=tick, daemon=True)
    thr.start()


def tick(queue_or_match=None):
    global time_bot_working, time_in_match, time_in_queue, error_handling_time
    thr = threading.currentThread()
    if queue_or_match is None:
        while getattr(thr, "do_run", True):
            time_bot_working += 1
            time.sleep(1)
    elif queue_or_match == "match":
        while getattr(thr, "do_run", True):
            time_in_match += 1
            time.sleep(1)
    elif queue_or_match == "queue":
        while getattr(thr, "do_run", True):
            time_in_queue += 1
            time.sleep(1)
    elif queue_or_match == "error":
        while getattr(thr, "do_run", True):
            error_handling_time += 1
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
    print("Time handling errors:", error_handling_time)
    if games_played == 0:
        print("Average search duration:",
              time.strftime("%M:%S", time.gmtime(time_in_queue)))
        print("Average match duration:",
              time.strftime("%M:%S", time.gmtime(time_in_match)))
    else:
        print("Average search duration:",
              time.strftime("%M:%S", time.gmtime(time_in_queue / games_played)))
        print("Average match duration:",
              time.strftime("%M:%S", time.gmtime((time_in_match - error_handling_time) / games_played)))
