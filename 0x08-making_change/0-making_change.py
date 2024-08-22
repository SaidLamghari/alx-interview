#!/usr/bin/python3
"""Auteur SAID AMGHARI"""


def makeChange(coins, total):
    """
    Calcule le nombre minimum de pièces nécessaires
    pour obtenir un montant donné.

    Cette fonction utilise une approche de
    programmation dynamique pour déterminer
    le nombre minimum de pièces nécessaires
    pour former un montant total avec un
    ensemble donné de pièces. Si le montant
    ne peut pas être atteint avec les
    pièces disponibles, la fonction
    retourne -1. Si le montant total est 0 ou
    inférieur, la fonction retourne 0.

    Paramètres:
    coins (list of int): Liste des dénominations des
                        pièces disponibles. Chaque
                        valeur dans la liste représente
                        une dénomination de pièce
                        et il y a une quantité illimitée
                        de chaque type de pièce.
    total (int): Montant total que l'on souhaite
                former avec les pièces. Il doit
                être un entier non négatif.

    Retourne:
    int: Nombre minimum de pièces nécessaires
    pour former le montant total.
         Retourne -1 si le montant total
         ne peut pas être formé avec les pièces
         disponibles. Retourne 0 si le montant
         total est 0 ou inférieur.

    Exemple:
    >>> makeChange([1, 2, 25], 37)
    7
    >>> makeChange([1256, 54, 48, 16, 102], 1453)
    -1

    Notes:
    - La fonction utilise une liste `vdb` où `vdb[i]`
        représente le nombre minimum de
        pièces nécessaires pour obtenir le montant `i`.
    - La complexité en temps de l'algorithme
        est O(n * m), où n est le nombre de
        dénominations de pièces et m est le montant total.
    - La complexité en espace est O(m),
    pour stocker la liste `vdb`.
    """
    # Cas de base : si le total est 0 ou négatif,
    # aucun jeton n'est nécessaire
    if total <= 0:
        return 0

    # Initialiser une liste pour stocker le nombre
    # minimum de pièces nécessaires pour chaque montant
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    # Zéro pièce nécessaire pour obtenir un total de 0

    # Itérer à travers chaque pièce et mettre à jour le tableau dp
    for coin in coins:
        for x in range(coin, total + 1):
            # Mettre à jour le nombre minimum de pièces
            # nécessaires pour obtenir le montant x
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # Si le total ne peut pas être atteint, retourner -1
    return dp[total] if dp[total] != float('inf') else -1
