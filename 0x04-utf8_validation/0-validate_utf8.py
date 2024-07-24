#!/usr/bin/python3
"""
Écrire une méthode qui détermine si un
ensemble de données donné représente un encodage UTF-8 valide.
Auteur SAID LAMGHARI
"""


def validUTF8(data):
    """
    Méthode pour déterminer si un ensemble de
    données donné représente un encodage UTF-8 valide.

    Args:
    data : List[int] - Liste d'entiers représentant les octets de données.

    Returns:
    bool - True si les données représentent
    un encodage UTF-8 valide, sinon False.
    """
    # Compte des octets restants à traiter pour le caractère UTF-8 actuel
    rmnng_bytes = 0

    # Parcourir chaque octet dans les données
    for nm in data:
        # Considérer uniquement les 8 bits les moins significatifs
        nm = nm & 0xFF

        # Si nous ne traitons pas encore un caractère UTF-8
        if rmnng_bytes == 0:
            # Déterminer le nombre d'octets du
            # caractère UTF-8 en fonction des bits de tête
            # Caractère 2 octets : commence par 110
            if (nm >> 5) == 0b110:
                rmnng_bytes = 1
            # Caractère 3 octets : commence par 1110
            elif (nm >> 4) == 0b1110:
                rmnng_bytes = 2
            # Caractère 4 octets : commence par 11110
            elif (nm >> 3) == 0b11110:
                rmnng_bytes = 3
            # Si le premier octet ne correspond à aucun format valide
            elif (nm >> 7):
                return False
        else:
            # Vérifier si l'octet de continuation commence par 10
            # Les octets de continuation doivent commencer par '10'
            if (nm >> 6) != 0b10:
                return False
            # Réduire le nombre d'octets restants à traiter
            rmnng_bytes -= 1

    # Si nous avons encore des octets
    # restants après avoir traité tous les octets
    # Cela signifie que la séquence est invalide
    return rmnng_bytes == 0
