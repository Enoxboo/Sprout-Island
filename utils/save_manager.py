import json
import os
from datetime import datetime

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAVE_FILE = os.path.join(PROJECT_ROOT, "savegame.json")


class SaveManager:
    @staticmethod
    def save_game(player, game_manager):
        save_data = {
            "player": {
                "name": player.name,
                "satiety": player.satiety,
                "hydration": player.hydration,
                "energy": player.energy
            },
            "game": {
                "days": game_manager.days
            },
            "timestamp": datetime.now().isoformat()
        }

        try:
            with open(SAVE_FILE, 'w', encoding='utf-8') as f:
                json.dump(save_data, f, indent=4, ensure_ascii=False)
            print(f"✓ Partie sauvegardée avec succès dans: {SAVE_FILE}")
            return True
        except Exception as e:
            print(f"✗ Erreur lors de la sauvegarde: {e}")
            return False

    @staticmethod
    def load_game():
        if not os.path.exists(SAVE_FILE):
            print(f"✗ Aucune sauvegarde trouvée à: {SAVE_FILE}")
            return None

        try:
            with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            print(f"✓ Partie chargée avec succès depuis: {SAVE_FILE}")
            return save_data
        except Exception as e:
            print(f"✗ Erreur lors du chargement: {e}")
            return None

    @staticmethod
    def delete_save():
        print(f"Tentative de suppression de: {SAVE_FILE}")

        if not os.path.exists(SAVE_FILE):
            print(f"✗ Le fichier n'existe pas: {SAVE_FILE}")
            return False

        try:
            os.remove(SAVE_FILE)

            if os.path.exists(SAVE_FILE):
                print(f"✗ ERREUR: Le fichier existe toujours après suppression!")
                return False

            print(f"✓ Sauvegarde supprimée avec succès: {SAVE_FILE}")
            return True
        except Exception as e:
            print(f"✗ Erreur lors de la suppression: {e}")
            return False

    @staticmethod
    def save_exists():
        exists = os.path.exists(SAVE_FILE)
        if exists:
            print(f"✓ Sauvegarde trouvée: {SAVE_FILE}")
        else:
            print(f"✗ Aucune sauvegarde: {SAVE_FILE}")
        return exists

    @staticmethod
    def load_player():
        if not SaveManager.save_exists():
            return None

        try:
            with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

            player_data = data['player']

            from models.player import Player
            player = Player(player_data['name'])
            player.satiety = player_data['satiety']
            player.hydration = player_data['hydration']
            player.energy = player_data['energy']

            print(f"✓ Joueur chargé: {player.name}")
            return player
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"✗ Erreur lors du chargement du joueur: {e}")
            return None