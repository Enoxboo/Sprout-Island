"""Fonctions utilitaires pour le jeu."""


def clamp(value, min_value, max_value):
    """Limite une valeur entre un minimum et un maximum."""
    return max(min_value, min(value, max_value))
