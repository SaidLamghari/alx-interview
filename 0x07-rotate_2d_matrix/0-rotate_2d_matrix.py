#!/usr/bin/python3
"""
Ce script fait pivoter une matrice 2D de n x n de 90
degrés dans le sens des aiguilles d'une montre.
La rotation est effectuée sur place (in-place).
"""


def rotate_2d_matrix(matrix):
    """
    Fait pivoter la matrice 2D donnée de 90 degrés dans
        le sens des aiguilles d'une montre, sur place.

    Paramètres:
    matrix (list of list of int): Une matrice 2D carrée
            (n x n) à faire pivoter.

    Retourne:
    None: La matrice est modifiée sur place,
        aucune nouvelle matrice n'est retournée.

    Description:
    La rotation se fait en deux étapes:
    1. Transposition de la matrice: Échange les éléments symétriques
        par rapport à la diagonale principale.
    2. Inversion des lignes: Inverse chaque ligne de la
        matrice transposée pour compléter la rotation.
    """
    # Nombre de lignes (ou colonnes) dans la matrice
    n = len(matrix)

    # Étape 1: Transposition de la matrice
    # La transposition échange les éléments
    # par rapport à la diagonale principale.
    for i in range(n):
        for j in range(i + 1, n):
            # Échange les éléments symétriques par rapport à la diagonale
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Étape 2: Inversion de chaque ligne
    # Chaque ligne de la matrice transposée est
    # inversée pour obtenir la rotation finale.
    for i in range(n):
        matrix[i].reverse()
