#!/usr/bin/python3
"""
Ce module contient une fonction qui calcule le nombre minimum d'opérations
nécessaires pour obtenir exactement n caractères H dans un fichier texte
en utilisant uniquement les opérations 'Tout Copier' et 'Coller'.
Auteur SAID LAMGHARI
"""

def minOperations(n):
    """
    Calcule le nombre minimum d'opérations nécessaires
    pour obtenir exactement n caractères H.
    
    Paramètres:
    n (int): Le nombre cible de caractères H.
    
    Retourne:
    int: Le nombre minimum d'opérations, ou 0 si n est impossible à atteindre.
    """
    # Si n est inférieur ou égal à 1, il est impossible
    # de l'atteindre avec les opérations données
    if (n <= 1):
        return 0
    
    # Initialisation des opérations à 0
    operatns = 0
    # Débuter avec le plus petit facteur premier
    fctr = 2
    
    # Boucle tant que n est supérieur à 1
    while n > 1:
        # Vérifier si n est divisible par le facteur courant
        while n % fctr == 0:
            # Ajouter le facteur au compte des opérations
            operatns += fctr
            # Diviser n par le facteur courant
            n //= fctr
        # Passer au facteur suivant
        fctr += 1
        
    return operatns
