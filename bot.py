import menu
import stats
import settings
import gameplay
import valorant


def main():
    print("___________________________________")
    print("Bot successfully started")
    print("Your screen resolution is " + str(settings.resolution_y) + "p\n")
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
        print("\nBot was manually stopped")
        stats.show()
        print("___________________________________")


main()
