from config import DAYS_TO_WIN
from models.player import Player


def run_game():
    game_over = False
    days = 0
    print("Tu te reveilles sur une île de prout et essaie de te souvenir de ton nom...")
    choice = input()
    player = Player(choice)
    while not game_over:
        print(f"Jour : {days}")
        print(f"Que faire aujourd'hui? ({' / '.join(player.actions.keys())})")
        choice = input()
        player.do_action(choice)
        days += 1
        if days == DAYS_TO_WIN:
            print("You won.")
            game_over = True
