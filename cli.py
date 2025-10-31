"""Interface en ligne de commande pour le jeu de survie sur une île déserte."""
from models.player import Player


def display_status(player):
    """Affiche le statut actuel du joueur."""
    print("\n" + "=" * 50)
    print(f"Joueur : {player.name}")
    print(f"Satiété : {player.satiety}/100")
    print(f"Hydratation : {player.hydration}/100")
    print(f"Énergie : {player.energy}/100")
    if player.rain_effect_days > 0:
        print(f"🌧️ Effet pluie actif ({player.rain_effect_days} jours restants)")
    if player.heatwave_effect_days > 0:
        print(f"🔥 Effet canicule actif ({player.heatwave_effect_days} jours restants)")
    print("=" * 50 + "\n")


def display_menu():
    """Affiche le menu des actions disponibles."""
    print("Actions disponibles :")
    print("1. Pêcher (fish)")
    print("2. Boire (drink)")
    print("3. Dormir (sleep)")
    print("4. Explorer (explore)")
    print("5. Quitter (quit)")
    print()


def get_user_choice():
    """Récupère le choix de l'utilisateur."""
    choice = input("Choisissez une action (1-5) : ").strip()
    actions = {
        "1": "fish",
        "2": "drink",
        "3": "sleep",
        "4": "explore",
        "5": "quit"
    }
    return actions.get(choice)


def main():
    """Fonction principale du jeu en CLI."""
    print("\n🏝️ Bienvenue sur l'île déserte ! 🏝️\n")
    name = input("Entrez votre nom : ").strip() or "Survivant"

    player = Player(name)
    day = 1

    print(f"\nBienvenue {player.name} ! Bonne chance pour survivre...")

    while not player.is_dead():
        print(f"\n--- Jour {day} ---")
        display_status(player)
        display_menu()

        action = get_user_choice()

        if action == "quit":
            print("\nVous abandonnez la survie. À bientôt !")
            break

        if action is None:
            print("❌ Action invalide. Veuillez réessayer.")
            continue

        result = player.do_action(action)

        if action == "fish":
            print("🎣 Vous avez pêché du poisson ! Satiété +, Énergie -")
        elif action == "drink":
            print("💧 Vous avez bu de l'eau ! Hydratation +, Énergie -")
        elif action == "sleep":
            print("😴 Vous vous êtes reposé ! Énergie +")
        elif action == "explore":
            print("🔍 Vous explorez l'île... Énergie -")

        if action != "sleep":
            player.apply_daily_losses()
            print("⏰ Fin de journée : pertes quotidiennes appliquées.")

        day += 1

    if player.is_dead():
        print("\n" + "=" * 50)
        print("💀 GAME OVER 💀")
        print(f"Vous avez survécu {day - 1} jour(s).")
        print("=" * 50)


if __name__ == "__main__":
    main()
