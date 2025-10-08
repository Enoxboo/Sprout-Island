from config import DAYS_TO_WIN
from models.player import Player


def run_game():
    game_over = False
    days = 0
    choice = input()
    player = Player(choice)
    while not game_over:
        choice = input()
        player.do_action(choice)
        days += 1
        if days == DAYS_TO_WIN:
            print("You won.")
            game_over = True
