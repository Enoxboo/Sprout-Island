import json
import os
from datetime import datetime

SAVE_FILE = "savegame.json"


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
            print("Partie sauvegardée avec succès!")
            return True
        except Exception as e:
            print(f"Erreur lors de la sauvegarde: {e}")
            return False

    @staticmethod
    def load_game():
        if not os.path.exists(SAVE_FILE):
            return None

        try:
            with open(SAVE_FILE, 'r', encoding='utf-8') as f:
                save_data = json.load(f)
            print("Partie chargée avec succès!")
            return save_data
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")
            return None

    @staticmethod
    def delete_save():
        if os.path.exists(SAVE_FILE):
            try:
                os.remove(SAVE_FILE)
                print("Sauvegarde supprimée.")
                return True
            except Exception as e:
                print(f"Erreur lors de la suppression: {e}")
                return False
        return False

    @staticmethod
    def save_exists():
        return os.path.exists(SAVE_FILE)