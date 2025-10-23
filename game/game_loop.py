from models.player import Player
from gui.main_window import MainWindow
from game.game_manager import GameManager



def run_game():
    game_manager = GameManager()

    print("Tu te réveilles sur une île de sprout et essaies de te souvenir de ton nom...")
    choice = input()
    player = Player(choice)
    game_windows = MainWindow(player)

    while not game_manager.is_game_over():
        print(f"Jour {game_manager.get_days()}")
        print(f"Que faire aujourd'hui ? ({' / '.join(player.actions.keys())})")
        game_windows.dialogue_frame.update_text("Que faire aujourd'hui ?")

        choice = game_windows.buttons_frame.get_player_choice()

        if choice in player.actions:
            player.do_action(choice)
            game_manager.increment_day()
            player.status()
            game_windows.status_frame.update_from_player()

            if game_manager.check_loss_condition(player):
                print("\nGame Over")
                game_windows.dialogue_frame.update_text("Game Over")
                break
            elif game_manager.check_win_condition():
                print("\nGagné")
                game_windows.dialogue_frame.update_text("Gagné")
                break
        else:
            print("Action inconnue ! Essaie encore.")
