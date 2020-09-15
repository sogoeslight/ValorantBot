import pyautogui

border = 31  # win application header/footer-borders (30px in FullHD, 40px in QHD, + 1px)
resolution_x = 1920
# resolution_x = pyautogui.size()[0]
resolution_y = 1080
# resolution_y = pyautogui.size()[1] + border

valorant_location = '"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant ' \
                    '--launch-patchline=live '
valorant_process_name = 'VALORANT-Win64-Shipping.exe'

# check yours and add 3 seconds
average_valorant_load_time = 24
average_match_load_time = 16

# it should close almost immediately, but for some reason it lives another second or two, so..
# only ints!!!
average_valorant_closing_time = 10

# Unrated = 0, Competitive = 1, Spike Rush = 2, DeathMatch = 3
# For now supposed to work only with DM tho, so
game_mode = 3
valorant_is_opened = True
first_game = True
enable_simulation = False
