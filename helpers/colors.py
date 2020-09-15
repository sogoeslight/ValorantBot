from colorthief import ColorThief

just_white = (255, 255, 255)

list_for_game_launch = [(36, 36, 44), (36, 44, 44), (29, 37, 44),
                        (40, 36, 44), (28, 37, 44)]
list_for_queing = [(36, 44, 44), (36, 36, 44), (29, 37, 44),
                   (40, 36, 44), (28, 37, 44)]
list_inactivity_message = [(44, 44, 52), (48, 44, 52)]
list_for_hovered_gun_in_buy = [(60, 196, 148), (12, 250, 164), (64, 196, 148)]
list_for_match_end = [(100, 196, 172), (68, 229, 185), (104, 196, 172)]
list_for_queing_again = [(44, 52, 60), (48, 52, 60), (42, 54, 66)]

list_generic_error = [(92, 92, 100), (96, 92, 100), (89, 93, 100)]
list_error_in_chat = [(124, 84, 84), (135, 67, 66)]


def compare_colors(colors, screenshot):
    # print("\n__________Start_____________")
    for color in colors:
        # print(color, ColorThief(screenshot).get_color(quality = 1))
        if color == ColorThief(screenshot).get_color(quality=1):
            return True

    # print("____________End_____________\n")
    return False
