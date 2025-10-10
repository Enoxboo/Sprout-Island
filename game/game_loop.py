from models.player import Player
from game.game_manager import GameManager


def run_game():
    game_manager = GameManager()

    print("Tu te réveilles sur une île de sprout et essaies de te souvenir de ton nom...")
    choice = input()
    player = Player(choice)

    while not game_manager.is_game_over():
        print(f"Jour {game_manager.get_days()}")
        print(f"Que faire aujourd'hui ? ({' / '.join(player.actions.keys())})")

        choice = input()

        if choice in player.actions:
            player.do_action(choice)
            game_manager.increment_day()
            player.status()

            if game_manager.check_loss_condition(player):
                print("\nGame Over")
                break
            elif game_manager.check_win_condition():
                print("\nGagné")
                break
        else:
            print("Action inconnue ! Essaie encore.")
