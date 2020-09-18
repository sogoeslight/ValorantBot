import menu
import settings
import gameplay
import valorant
import stats


def main():
    print("\nBot successfully started")
    # stats.compose_stats()
    if not settings.valorant_is_opened:
        valorant.launch()
        settings.valorant_is_opened = True

    while True:
        if settings.first_game:
            menu.start_game()
            settings.first_game = False

        gameplay.simulate(settings.enable_simulation)

        menu.play_again()


main()
