import time
import threading

experience_farmed = 0
time_bot_working = 0
time_in_queue = 0
time_in_match = 0
games_played = 0


def timer():
    thr = threading.Thread(target=tick, daemon=True)
    thr.start()


def tick():
    global time_bot_working
    while True:
        time_bot_working += 1
        time.sleep(1)


def count_game():
    global games_played
    games_played += 1


def count_queue_time(time_in_seconds):
    global time_in_queue
    time_in_queue += time_in_seconds


def count_match_time(time_in_seconds):
    global time_in_match
    time_in_match += time_in_seconds


def show_current_time():
    print("Current Time =", time.strftime("%H:%M:%S", time.localtime()))


def show():
    print("XP farmed:", games_played * 500)
    print("Time working:", time_bot_working)
    try:
        print("Average search duration:", time.strftime("%M:%S", time.gmtime(time_in_queue / games_played)))
        print("Average match duration:", time.strftime("%M:%S", time.gmtime(time_in_match / games_played)))
    except ZeroDivisionError:
        print("Stats did not work properly. Can not divide by zero")
