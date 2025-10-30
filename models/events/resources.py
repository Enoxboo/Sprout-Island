"""Événements de découverte de ressources."""
from config import (FRUIT_SATIETY_GAIN, FRUIT_HYDRATION_GAIN,
                    SATIETY_MAX, HYDRATION_MAX)
from models.events.base import Event
from utils.helpers import clamp

class FindFruitEvent(Event):
    def __init__(self):
        super().__init__(
            "Fruits sauvages",
            "Vous découvrez des fruits comestibles!"
        )

    def trigger(self, player):
        old_satiety = player.satiety
        old_hydration = player.hydration

        player.satiety = clamp(
            player.satiety + FRUIT_SATIETY_GAIN,
            0,
            SATIETY_MAX
        )
        player.hydration = clamp(
            player.hydration + FRUIT_HYDRATION_GAIN,
            0,
            HYDRATION_MAX
        )

        actual_satiety = player.satiety - old_satiety
        actual_hydration = player.hydration - old_hydration

        return {
            "message": (
                f"🥭 {self.description}\n\n"
                f"Vous trouvez des fruits juteux et sucrés dans les buissons.\n"
                f"🍖 Satiété +{actual_satiety}\n"
                f"💧 Hydratation +{actual_hydration}"
            ),
            "type": "positive"
        }
