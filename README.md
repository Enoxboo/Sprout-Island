# 🏝️ Sprout Island


Un jeu de survie sur une île déserte développé en Python avec Tkinter.

## 📝 Description

Sprout Island est un jeu de survie basé sur des choix où vous devez gérer vos ressources pour survivre sur une île déserte pendant 20 jours. Gérez votre faim, votre hydratation et votre énergie en faisant des choix stratégiques chaque jour.

## ✨ Fonctionnalités

-  Interface graphique intuitive avec Tkinter
-  Système de gestion de ressources (Satiété, Hydratation, Énergie)
-  Objectif : Survivre 20 jours sur l'île
-  Système de sauvegarde et chargement de partie
-  Interface utilisateur personnalisée avec boutons stylisés
-  Barres de statut en temps réel
-  Système d'actions multiples (Pêcher, Boire, Dormir, Explorer)

## 🎯 Objectif du jeu

Survivez **20 jours** sur l'île en maintenant vos statistiques au-dessus de zéro :
- **Satiété** : Ne pas mourir de faim
- **Hydratation** : Rester hydraté
- **Énergie** : Conserver assez d'énergie pour agir

## 🕹️ Actions disponibles

| Action | Effet |
|--------|-------|
| 🎣 **Pêcher** | +25 Satiété, -20 Énergie |
| 💧 **Boire** | +30 Hydratation, -20 Énergie |
| 😴 **Dormir** | +50 Énergie, -10 Satiété, -15 Hydratation |
| 🔍 **Explorer** | À découvrir... |

## 🚀 Installation

### Prérequis

- Python 3.8 ou supérieur
- tkinter (généralement inclus avec Python)


### Cloner le projet

```bash
git clone https://github.com/votre-username/Sprout-Island.git
cd Sprout-Island
```

## ▶️ Lancement du jeu

```bash
python main.py
```

## 📁 Structure du projet

```
Sprout-Island/
├── main.py                 # Point d'entrée du jeu
├── config.py              # Configuration des paramètres du jeu
├── savegame.json          # Fichier de sauvegarde
├── LICENSE                # Licence du projet
├── README.md              # Ce fichier
│
├── game/                  # Logique du jeu
│   ├── game_loop.py      # Boucle principale du jeu
│   └── game_manager.py   # Gestionnaire de l'état du jeu
│
├── gui/                   # Interface graphique
│   ├── main_window.py    # Fenêtre principale
│   ├── start_frame.py    # Écran de démarrage
│   ├── button_frame.py   # Boutons d'action
│   ├── dialogue_frame.py # Zone de dialogue
│   └── status_frame.py   # Barres de statut
│
├── models/                # Modèles de données
│   └── player.py         # Classe joueur
│
├── utils/                 # Utilitaires
│   ├── helpers.py        # Fonctions helper
│   └── save_manager.py   # Gestion des sauvegardes
│
├── tests/                 # Tests unitaires
│   ├── test_game_manager.py
│   └── test_player.py
│
└── src/                   # Ressources (images, icônes)
    └── teemo_basic.ico
```

## 🎮 Comment jouer

1. **Démarrer une nouvelle partie** : Entrez votre nom et cliquez sur "Nouvelle Partie"
2. **Charger une partie** : Cliquez sur "Charger" pour reprendre votre dernière sauvegarde
3. **Gérer vos ressources** : Choisissez vos actions avec prudence
4. **Survivre** : Maintenez toutes vos statistiques au-dessus de 0 pendant 20 jours
5. **Victoire** : Survivez les 20 jours pour gagner !

## ⚙️ Configuration

Les paramètres du jeu peuvent être modifiés dans `config.py` :

```python
SATIETY_MAX = 100        # Satiété maximale
HYDRATION_MAX = 100      # Hydratation maximale
ENERGY_MAX = 100         # Énergie maximale
DAYS_TO_WIN = 20         # Jours nécessaires pour gagner
```

## 🧪 Tests

Pour exécuter les tests unitaires :

```bash
python -m pytest tests/
```

Ou individuellement :

```bash
python -m pytest tests/test_player.py
python -m pytest tests/test_game_manager.py
```

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

[**Matteo Marquant**](https://github.com/Enoxboo)
 
[**Alexandre RIVIERE**](https://github.com/AlexandreRiv)



**Bon jeu et bonne survie sur Sprout Island ! 🏝️**

