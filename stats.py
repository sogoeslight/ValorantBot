from datetime import datetime

experience_farmed = 0
time_bot_working = 0
average_search_duration = 0
average_match_duration = 0


def inc_exp(exp=500):
    experience_farmed += exp


def count_game():
    games_played += 1


def count_time(time):
    self.time_in_queue += time


def show_current_time():
    now = datetime.now()
    print("Current Time =", now.strftime("%H:%M:%S"))


def show():
    print("XP farmed:", experience_farmed)
    print("Time working:", time_bot_working)
    print("Average search duration:", average_search_duration)
    print("Average match duration:", average_match_duration)