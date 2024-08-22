#!/usr/bin/python3
"""Module pour la gestion des pièces de monnaie.
Ce module contient une fonction pour déterminer
le nombre minimum de pièces
nécessaires pour obtenir un montant donné en
utilisant un ensemble de pièces de différentes valeurs.
Auteur SAID LAMGHARI
"""


def makeChange(coins, total):
    """
    Détermine le nombre minimum de pièces nécessaires
    pour obtenir un montant total donné
    lorsqu'on dispose d'un ensemble de pièces de différentes
    valeurs. Utilise un algorithme glouton
    en choisissant toujours la pièce de plus grande valeur disponible.

    Paramètres:
    coins (list of int): Liste d'entiers représentant
    les valeurs des pièces disponibles.
    total (int): Montant total à atteindre.

    Retourne:
    int: Le nombre minimum de pièces nécessaires pour
    obtenir le montant total. Retourne -1
         si le montant total ne peut pas être atteint
         avec les pièces disponibles.

    Notes:
    - Cette implémentation utilise un algorithme glouton,
    qui peut ne pas fonctionner dans tous les cas.
      Par exemple, avec des pièces {1, 3, 4} et un montant
      de 6 (la solution correcte est 2 pièces: 3+3),
      l'algorithme glouton retournerait 3 pièces: 4+1+1.
    - La complexité temporelle est O(n log n) en raison du tri
    des pièces, où n est le nombre de dénominations de pièces.
    """

    # Cas particulier : si le montant total est 0 ou inférieur
    if total <= 0:
        return 0

    # Trie les pièces par ordre décroissant
    sortdCoins = sorted(coins, reverse=True)

    # Initialisation des variables
    rst = total  # Montant restant à obtenir
    coinsCount = 0  # Compteur pour le nombre de pièces utilisées

    # Processus pour obtenir la monnaie
    for cn in sortdCoins:
        while rst >= cn:
            rst -= cn
            coinsCount += 1

    # Si après avoir utilisé toutes les pièces
    # disponibles, il reste encore un montant
    if rst > 0:
        return -1

    return coinsCount
