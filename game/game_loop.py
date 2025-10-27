from models.player import Player
from gui.main_window import MainWindow
from game.game_manager import GameManager
from utils.save_manager import SaveManager


def run_game():
    game_manager = GameManager()
    player = None

    if SaveManager.save_exists():
        print("Une sauvegarde a été trouvée!")
        choice = input("Voulez-vous charger la partie sauvegardée? (oui/non): ").lower()

        if choice in ['oui', 'o', 'yes', 'y']:
            save_data = SaveManager.load_game()
            if save_data:
                player = Player(save_data['player']['name'])
                player.satiety = save_data['player']['satiety']
                player.hydration = save_data['player']['hydration']
                player.energy = save_data['player']['energy']

                game_manager.days = save_data['game']['days']

                print(f"Partie de {player.name} chargée! Jour {game_manager.days}")
        else:
            SaveManager.delete_save()

    if player is None:
        print("Tu te réveilles sur une île de sprout et essaies de te souvenir de ton nom...")
        choice = input()
        player = Player(choice)

    game_windows = MainWindow(player)

    while not game_manager.is_game_over():
        print(f"Jour {game_manager.get_days()}")
        print(f"Que faire aujourd'hui ? ({' / '.join(player.actions.keys())} / quit)")
        game_windows.dialogue_frame.update_text("Que faire aujourd'hui ?")

        choice = game_windows.buttons_frame.get_player_choice()

        if choice == "quit":
            SaveManager.save_game(player, game_manager)
            print("Partie sauvegardée. À bientôt!")
            break

        if choice in player.actions:
            player.do_action(choice)
            game_manager.increment_day()
            player.status()
            game_windows.status_frame.update_from_player()

            SaveManager.save_game(player, game_manager)

            if game_manager.check_loss_condition(player):
                print("\nGame Over")
                game_windows.dialogue_frame.update_text("Game Over")
                SaveManager.delete_save()
                break
            elif game_manager.check_win_condition():
                print("\nGagné")
                game_windows.dialogue_frame.update_text("Gagné")
                SaveManager.delete_save()
                break
        else:
            print("Action inconnue ! Essaie encore.")
