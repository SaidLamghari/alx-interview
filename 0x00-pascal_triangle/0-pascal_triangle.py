#!/usr/bin/python3
"""
Autor: SAID LAMGHARI
"""


def pascal_triangle(n):
    """
    Génère un triangle de Pascal jusqu'à la ligne n-ème (inclusive).

    Args:
    - n (int): Nombre de lignes du triangle de Pascal à générer.

    Returns:
    - list: Liste de listes représentant
            le triangle de Pascal jusqu'à la ligne n.
            Chaque sous-liste représente une ligne du triangle.

    Exemple:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """

    if n <= 0:
        return []

    triangle = [[1]]  # Initialise le triangle avec la première ligne

    for i in range(1, n):
        row = [1]  # Chaque ligne commence et termine par 1
        for j in range(1, i):
            # Calcule les valeurs intérieures de la ligne
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Termine la ligne avec 1
        triangle.append(row)  # Ajoute la ligne au triangle

    return triangle
