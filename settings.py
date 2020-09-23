import pyautogui

# detect screen resolution
resolution_x = pyautogui.size()[0]
resolution_y = pyautogui.size()[1]

if resolution_y == 1080:
    resolution_string = "FullHD"
    border = 31  # win application header/footer-borders + 1px
elif resolution_y == 1440:
    resolution_string = "QHD"
    border = 20

safe_point = resolution_x * 0.88, resolution_y * 0.12, 60, 13

valorant_location = '"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant ' \
                    '--launch-patchline=live '
valorant_process_name = 'VALORANT-Win64-Shipping.exe'

average_valorant_load_time = 22
average_match_load_time = 16
checks_refresh_rate = 1
# Increase it a bit if CMD lags sometimes
system_animations_time = .7

# For some reason Valorant process lives another few seconds, so..
average_valorant_closing_time = 12  # only ints!!!

# Unrated = 0, Competitive = 1, Spike Rush = 2, DeathMatch = 3
# For now supposed to work only with DM tho, so
game_mode = 3
valorant_is_opened = True
first_game = True
was_relaunched_after_error = False
enable_simulation = False
