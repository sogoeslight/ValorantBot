import menu
import stats
import settings
import gameplay
import valorant
import ingame_error
from datetime import datetime
from colorama import init, Fore


def main():
    stats.starting_work_time = datetime.now()
    init()
    print(Fore.RED + "__" + Fore.LIGHTRED_EX + "____" + Fore.LIGHTYELLOW_EX
          + "_____" + Fore.LIGHTGREEN_EX + "____" + Fore.GREEN + "____"
          + Fore.LIGHTBLUE_EX + "____" + Fore.CYAN
          + "_____" + Fore.LIGHTMAGENTA_EX + "___" + Fore.MAGENTA + "____\n")
    print(Fore.RED + "Bo" + Fore.LIGHTRED_EX + "t ha" + Fore.LIGHTYELLOW_EX
          + "s bee" + Fore.LIGHTGREEN_EX + "n suc" + Fore.GREEN + "ces"
          + Fore.LIGHTBLUE_EX + "sful" + Fore.CYAN
          + "ly st" + Fore.LIGHTMAGENTA_EX + "art" + Fore.MAGENTA + "ed!")
    print(Fore.WHITE + "Your screen resolution is " + Fore.CYAN + str(settings.resolution_y) + "p")
    print(Fore.WHITE + "Current time is", end='')
    stats.show_current_time()
    print(Fore.WHITE + "To stop bot execution press " + Fore.LIGHTRED_EX + "'ctrl+c'\n" + Fore.LIGHTGREEN_EX)
    ingame_error.checker_thread()
    try:
        if not settings.valorant_is_opened:
            valorant.launch()
            settings.valorant_is_opened = True

        while True:
            if settings.first_game:
                menu.start_game()
                settings.first_game = False

            gameplay.simulate(settings.enable_simulation)
            if settings.was_relaunched_after_error:
                settings.was_relaunched_after_error = False
                menu.start_game()
            else:
                menu.play_again()
    except KeyboardInterrupt:
        ingame_error.close_thread()
        print(Fore.YELLOW + "\nBot was manually stopped")
        stats.show()
        print(Fore.RED + "__" + Fore.LIGHTRED_EX + "____" + Fore.LIGHTYELLOW_EX
              + "_____" + Fore.LIGHTGREEN_EX + "____" + Fore.GREEN + "____"
              + Fore.BLUE + "____" + Fore.LIGHTBLUE_EX + "___" + Fore.CYAN
              + "__" + Fore.LIGHTMAGENTA_EX + "___" + Fore.MAGENTA + "____\n")
        print(Fore.LIGHTBLACK_EX + "Contacts:")
        print(Fore.LIGHTBLACK_EX + "   - https://github.com/SoGoesLight")
        print(Fore.LIGHTBLACK_EX + "   - SoGoesLight@gmail.com")


main()
