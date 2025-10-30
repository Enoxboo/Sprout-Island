"""Événements météorologiques (pluie, canicule)."""
from config import HYDRATION_MAX, ENERGY_MAX
from models.events.base import Event


class RainEvent(Event):
    def __init__(self):
        super().__init__(
            "Pluie rafraîchissante",
            "Une pluie bienfaisante commence à tomber sur l'île."
        )

    def trigger(self, player):
        from config import RAIN_HYDRATION_GAIN, RAIN_DURATION, HYDRATION_MAX
        from utils.helpers import clamp

        old_hydration = player.hydration
        player.hydration = clamp(
            player.hydration + RAIN_HYDRATION_GAIN,
            0,
            HYDRATION_MAX
        )
        gain = player.hydration - old_hydration
        player.rain_effect_days = RAIN_DURATION

        return {
            "message": (
                f"☔ {self.description}\n\n"
                f"Vous collectez de l'eau fraîche dans vos mains.\n"
                f"💧 Hydratation +{gain}\n"
                f"🌧️ Pluie continue pendant {RAIN_DURATION} jours (pas de perte d'hydratation quotidienne)"
            ),
            "type": "positive"
        }


class HeatwaveEvent(Event):
    def __init__(self):
        super().__init__(
            "Canicule accablante",
            "Une vague de chaleur intense s'abat sur l'île!"
        )

    def trigger(self, player):
        from config import HEATWAVE_HYDRATION_LOSS, HEATWAVE_ENERGY_LOSS, HEATWAVE_DURATION, HYDRATION_MIN, ENERGY_MIN
        from utils.helpers import clamp

        old_hydration = player.hydration
        old_energy = player.energy

        player.hydration = clamp(
            player.hydration - HEATWAVE_HYDRATION_LOSS,
            HYDRATION_MIN,
            HYDRATION_MAX
        )
        player.energy = clamp(
            player.energy - HEATWAVE_ENERGY_LOSS,
            ENERGY_MIN,
            ENERGY_MAX
        )

        actual_hydration_loss = old_hydration - player.hydration
        actual_energy_loss = old_energy - player.energy
        player.heatwave_effect_days = HEATWAVE_DURATION

        return {
            "message": (
                f"🌡️ {self.description}\n\n"
                f"Le soleil brûlant vous épuise rapidement.\n"
                f"💧 Hydratation -{actual_hydration_loss}\n"
                f"⚡ Énergie -{actual_energy_loss}\n"
                f"☀️ Canicule continue pendant {HEATWAVE_DURATION} jours (-10 hydratation/jour)"
            ),
            "type": "negative"
        }
