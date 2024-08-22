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

    # Cas particulier : si le montant est 0 ou inférieur
    if total <= 0:
        return 0

    # Initialisation de la liste vdb avec
    # une valeur infinie, sauf vdb[0] = 0
    # vdb[i] représente le nombre minimum de
    # pièces nécessaires pour obtenir le montant i
    vdb = [float('inf')] * (total + 1)
    vdb[0] = 0
    # 0 pièces sont nécessaires pour obtenir le montant 0

    # Traitement de chaque pièce
    for coin in coins:
        # On parcourt les montants à partir de la
        # valeur de la pièce jusqu'au montant total
        for amount in range(coin, total + 1):
            # Si le montant (amount - coin) peut
            # être atteint, alors il est possible de
            # former le montant 'amount' en ajoutant la pièce actuelle
            if vdb[amount - coin] != float('inf'):
                # Met à jour le nombre minimum
                # de pièces pour le montant 'amount'
                vdb[amount] = min(vdb[amount], vdb[amount - coin] + 1)

    # Si vdb[total] est encore infini, cela
    # signifie que le montant total ne peut pas être
    # atteint avec les pièces disponibles
    return vdb[total] if vdb[total] != float('inf') else -1
