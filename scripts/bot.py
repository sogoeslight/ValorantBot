import menu
import stats
import settings
import gameplay
import valorant
from colorama import init, Fore


def main():
    init()
    print(Fore.YELLOW + "____________________________________")
    print(Fore.WHITE + "Bot successfully started!")
    print("Your screen resolution is " + Fore.CYAN + str(settings.resolution_y) + "p")
    print(Fore.WHITE + "To stop bot execution press " + Fore.LIGHTRED_EX + "'ctrl+c'\n" + Fore.LIGHTGREEN_EX)
    stats.daemon_timer()
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
        print(Fore.YELLOW + "\nBot was manually stopped")
        stats.show()
        print(Fore.YELLOW + "____________________________________")
        print(Fore.LIGHTBLACK_EX + "Contacts:")
        print(Fore.LIGHTBLACK_EX + "   - https://github.com/SoGoesLight")
        print(Fore.LIGHTBLACK_EX + "   - SoGoesLight@gmail.com")


main()
