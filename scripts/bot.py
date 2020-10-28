import menu
import stats
import settings
import gameplay
import valorant
from colorama import init, Fore


def main():
    init()
    print(Fore.YELLOW + "___________________________________")
    print(Fore.WHITE + "Bot successfully started!" + Fore.WHITE)
    print("Your screen resolution is " + Fore.CYAN + str(settings.resolution_y) + "p\n" + Fore.GREEN)
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
            print("2")
            if settings.was_relaunched_after_error:
                settings.was_relaunched_after_error = False
                menu.start_game()
            else:
                print("3")
                menu.play_again()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nBot was manually stopped")
        stats.show()
        print(Fore.YELLOW + "___________________________________")


main()
