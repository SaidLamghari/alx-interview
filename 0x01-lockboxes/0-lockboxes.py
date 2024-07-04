#!/usr/bin/python3


def canUnlockAll(boxes):
    """
    Détermine si toutes les boîtes peuvent être ouvertes.

    Args:
    boxes (list of list of int): Une liste où chaque élément est
    une liste de clés contenues dans la boîte correspondante.

    Returns:
    bool: True si toutes les boîtes peuvent être ouvertes, False sinon.
    """
    n = len(boxes)
    # Initialiser un tableau pour suivre l'état des boîtes déverrouillées
    unlocked = [False] * n
    # La première boîte est toujours déverrouillée au départ
    unlocked[0] = True
    stack = [0]  # Utiliser une pile pour suivre les boîtes à visiter

    while stack:
        current_box = stack.pop()  # Récupérer la boîte actuelle
        for key in boxes[current_box]:
            # Vérifier si la clé est valide
            # si la boîte n'est pas déjà déverrouillée
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True  # Déverrouiller la boîte
                # Ajouter la boîte à la pile des boîtes à visiter
                stack.append(key)

    # Vérifier si toutes les boîtes ont été déverrouillées
    return all(unlocked)
