#!/usr/bin/python3
"""
Write a method that determines if a
given data set represents a valid UTF-8 encoding.
Auteur SAID LAMGHARI
"""


def validUTF8(data):
    """
    Méthode pour déterminer si un ensemble de données
    donné représente un encodage UTF-8 valide.

    Args:
    data : List[int] - Liste d'entiers représentant les octets de données.

    Returns:
    bool - True si les données représentent
    un encodage UTF-8 valide, sinon False.
    """

    # Nombre de btes dans le caractère UTF-8 actuel
    nm_byts = 0

    # Masques pour vérifier
    # le nombre de '1' en tête dans un bte
    msks = [
        0b10000000,  # 1 '1' en tête
        0b11100000,  # 3 '1' en tête
        0b11110000,  # 4 '1' en tête
        0b11111000   # 5 '1' en tête
    ]

    # Marqueurs pour extraire les bits significatifs
    mrkrs = [
        0b00000000,  # 1 '0' en tête
        0b11000000,  # 2 '1' en tête
        0b11100000,  # 3 '1' en tête
        0b11110000,  # 4 '1' en tête
        0b11111000   # 5 '1' en tête
    ]

    # Parcourir chaque bte dans les données
    for bte in data:
        # Ne considérerque les 8 bits de poids faible
        bte = bte & 0xFF

        if nm_byts == 0:
            # Déterminer combien de btes
            # le caractère UTF-8 devrait couvrir
            for i in range(len(msks)):
                if bte & msks[i] == mrkrs[i]:
                    nm_byts = i
                    break
            if nm_byts == 0:
                continue
            if nm_byts == 1 or nm_byts > 4:
                return False
        else:
            # Vérifier si le bte commence par '10'
            if bte & 0b11000000 != 0b10000000:
                return False

        nm_byts -= 1

    # Vérifier s'il ne reste aucun bte à traiter
    return nm_byts == 0
