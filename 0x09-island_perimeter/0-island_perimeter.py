#!/usr/bin/python3
"""
0. Périmètre de l'île
Auteur SAID LAMGHARI
"""


def island_perimeter(grid):
    """
    Calcule le périmètre de l'île décrite dans la grille.

    Args:
    grid (list de list d'entiers): Grille 2D représentant la carte où
                                   0 représente l'eau et 1 représente la terre.

    Returns:
    int: Le périmètre de l'île.
    """
    # Vérifie si la grille est vide, auquel cas le périmètre est 0.
    if not grid:
        return 0

    # Obtient le nombre de lignes (hauteur) et
    # de colonnes (largeur) de la grille.
    hautr = len(grid)
    largr = len(grid[0])

    # Initialise le compteur de périmètre à 0.
    primtre = 0

    # Définir les directions pour
    # vérifier les cellules adjacentes:
    # (droite, gauche, bas, haut).
    dirctons = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Parcourt chaque cellule de la grille.
    for i in range(hautr):
        for j in range(largr):
            # Si la cellule actuelle est une cellule de terre (1),
            # on vérifie les cellules adjacentes.
            if grid[i][j] == 1:
                # Pour chaque cellule de terre,
                # vérifie les 4 directions adjacentes.
                for di, dj in dirctons:
                    # Calculer les coordonnées de la cellule voisine.
                    ni, nj = i + di, j + dj

                    # Vérifie si la cellule voisine est
                    # à l'intérieur des limites de la grille.
                    if (0 <= ni < hautr) and (0 <= nj < largr):
                        # Si la cellule voisine est de l'eau (0),
                        # ou si elle est une cellule
                        # de terre (1) mais adjacent à l'eau,
                        # incrémente le périmètre pour ce côté.
                        if grid[ni][nj] == 0:
                            primtre += 1
                    else:
                        # Si la cellule voisine est hors des
                        # limites de la grille (bord extérieur),
                        # cela signifie que ce côté
                        # est exposé à l'eau extérieure,
                        # donc incrémente le périmètre pour ce côté.
                        primtre += 1

    # Retourne le périmètre total de l'île.
    return primtre
