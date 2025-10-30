from game.game_loop import run_game

"""
Point d'entrée principal du jeu Sprout Island.
Lance la boucle de jeu avec l'interface graphique.
"""
if __name__ == '__main__':
    try:
        run_game()
    except Exception as e:
        print(f"Erreur fatale: {e}")
        import traceback

        traceback.print_exc()
