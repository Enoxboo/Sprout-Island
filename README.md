# 🏝️ Sprout Island

Un jeu de survie sur une île déserte développé en Python avec Tkinter.

## 📝 Description

Sprout Island est un jeu de survie basé sur des choix où vous devez gérer vos ressources pour survivre sur une île déserte pendant 20 jours. Gérez votre faim, votre hydratation et votre énergie en faisant des choix stratégiques tout en affrontant des événements aléatoires (météo, animaux sauvages, découvertes).

## ✨ Fonctionnalités

- 🎨 Interface graphique intuitive avec Tkinter
- 📊 Système de gestion de ressources (Satiété, Hydratation, Énergie)
- 🎯 Objectif : Survivre 20 jours sur l'île
- 💾 Système de sauvegarde et chargement de partie
- 🎨 Interface utilisateur personnalisée avec boutons stylisés
- 📈 Barres de statut en temps réel
- 🎮 Système d'actions multiples (Pêcher, Boire, Dormir, Explorer)
- 🌦️ Événements aléatoires avec effets durables (pluie, canicule, animaux, ressources)
- ⚖️ Système d'événements équilibré avec exclusion mutuelle météorologique

## 🎯 Objectif du jeu

Survivez **20 jours** sur l'île en maintenant vos statistiques au-dessus de zéro :
- **Satiété** : Ne pas mourir de faim (-12/jour)
- **Hydratation** : Rester hydraté (-15/jour, modifié par la météo)
- **Énergie** : Conserver assez d'énergie pour agir (-8/jour)

## 🕹️ Actions disponibles

| Action | Effet |
|--------|-------|
| 🎣 **Pêcher** | +35 Satiété, -15 Énergie |
| 💧 **Boire** | +40 Hydratation, -10 Énergie |
| 😴 **Dormir** | +70 Énergie |
| 🔍 **Explorer** | -20 Énergie, déclenche des événements aléatoires |

## 🌟 Événements aléatoires

### Événements météorologiques
- **☔ Pluie rafraîchissante** : +35 Hydratation, pas de perte d'hydratation pendant 3 jours
- **🌡️ Canicule accablante** : -25 Hydratation, -15 Énergie, -10 Hydratation/jour pendant 3 jours

### Événements de faune
- **🐗 Rencontre animale** : Choix entre fuir (-30 Énergie) ou chasser (-40 Énergie, +55 Satiété)

### Événements de ressources
- **🥭 Fruits sauvages** : +20 Satiété, +15 Hydratation

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
py main.py
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
│   ├── status_frame.py   # Barres de statut
│   └── shapes.py         # Formes personnalisées (rectangles arrondis)
│
├── models/                # Modèles de données
│   ├── player.py         # Classe joueur
│   └── events/           # Système d'événements modulaire
│       ├── __init__.py   # Exports du package
│       ├── base.py       # Classe abstraite Event
│       ├── manager.py    # Gestionnaire d'événements
│       ├── weather.py    # Événements météo (pluie, canicule)
│       ├── wildlife.py   # Événements animaux
│       └── resources.py  # Événements de ressources
│
├── utils/                 # Utilitaires
│   ├── helpers.py        # Fonctions helper (clamp)
│   └── save_manager.py   # Gestion des sauvegardes
│
├── tests/                 # Tests unitaires
│   ├── test_game_manager.py
│   ├── test_player.py
│   └── test_event.py     # Tests du système d'événements
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

## 📜 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

[**Matteo Marquant**](https://github.com/Enoxboo)
 
[**Alexandre RIVIERE**](https://github.com/AlexandreRiv)



**Bon jeu et bonne survie sur Sprout Island ! 🏝️**

