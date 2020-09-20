from colorthief import ColorThief

almost_white = (251, 251, 251)

list_for_game_launch = [(223, 223, 237), (36, 36, 44), (36, 44, 44), (29, 37, 44),
                        (40, 36, 44), (28, 37, 44)]

list_for_game_launch_in_match = [(214, 213, 212), (215, 214, 213)]

list_for_party_not_ready = [(53, 37, 44), (52, 36, 44), (60, 35, 39),
                            (94, 83, 86), (68, 51, 52), (72, 63, 64), (23, 24, 28)]
list_inactivity_message = [(44, 44, 52), (48, 44, 52)]
list_for_hovered_gun_in_buy = [(173, 197, 189), (63, 195, 148), (60, 196, 148),
                               (12, 250, 164), (64, 196, 148)]
list_for_match_end = [(100, 196, 172), (68, 229, 185), (104, 196, 172)]

list_generic_error = [(91, 91, 99), (92, 92, 100), (96, 92, 100), (89, 93, 100)]
list_error_in_chat = [(124, 84, 84), (135, 67, 66)]


def compare_colors(colors, screenshot, tolerance=2):
    # print("\n__________Start_____________")
    for color in colors:
        screenshot_color = ColorThief(screenshot).get_color(quality=1)
        # print(color, screenshot_color, "tolerance =", tolerance)
        if ((abs(color[0] - screenshot_color[0]) < tolerance)
                & ((abs(color[1] - screenshot_color[1])) < tolerance)
                & ((abs(color[2] - screenshot_color[2])) < tolerance)):
            return True

    # print("___________End______________\n")
    return False


# def compare_colors1(colors, screenshot, tolerance=3):
#     print("\n__________Start_____________")
#     for color in colors:
#         print(color, ColorThief(screenshot).get_color(quality=1))
#         if color == ColorThief(screenshot).get_color(quality=1):
#             return True
#
#     print("___________End______________\n")
#     return False
