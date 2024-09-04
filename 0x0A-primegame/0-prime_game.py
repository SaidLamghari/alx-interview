#!/usr/bin/python3
"""
Jeu des Nombres Premiers
Auteur : SAID LAMGHARI
"""


def funct_sieve(max_val):
    """
    Génère une liste de nombres premiers jusqu'à max_val en utilisant
    l'algorithme du Crible d'Ératosthène.

    :param max_val: Valeur maximale
    jusqu'à laquelle les nombres premiers
    doivent être générés.
    :return: Liste de nombres premiers jusqu'à max_val.
    """
    # Liste pour marquer les nombres premiers (initialement, tous les
    # nombres sont supposés premiers)
    valprime = [True] * (max_val + 1)
    p = 2

    while p * p <= max_val:
        if valprime[p]:
            # Marque tous les multiples de p comme non premiers
            for i in range(p * p, max_val + 1, p):
                valprime[i] = False
        p += 1

    # Retourne la liste des nombres premiers
    return [p for p in range(2, max_val + 1) if valprime[p]]


def is_winner(x, nums):
    """
    Détermine le gagnant du jeu
    des nombres premiers après x tours.

    :param x: Nombre de tours de jeu.
    :param nums: Liste des valeurs de n pour chaque tour de jeu.
    :return: Nom du joueur ayant gagné
    le plus de tours ("Maria" ou "Ben"),
    ou None si les deux joueurs ont
    gagné un nombre égal de tours.
    """
    from bisect import bisect_right

    # Trouve la valeur maximale de n pour optimiser la génération des
    # nombres premiers
    val_maxn = max(nums)
    # Génère tous les nombres premiers jusqu'à la valeur maximale de n
    primes = funct_sieve(val_maxn)

    def playgame(n):
        """
        Simule un tour de jeu pour une valeur donnée de n et détermine le
        gagnant du tour.

        :param n: Valeur de n pour le tour de jeu.
        :return: Nom du gagnant du tour de jeu ("Maria" ou "Ben").
        """
        if n < 2:
            # Si n < 2, il n'y a pas de nombres premiers disponibles,
            # donc Ben gagne par défaut
            return "Ben"

        # Ensemble des nombres premiers jusqu'à n
        prime_set = set(primes[:bisect_right(primes, n)])
        # 0 pour Maria, 1 pour Ben (Maria commence en premier)
        turn = 0

        while prime_set:
            # Choisit le plus petit nombre premier disponible
            prime = min(prime_set)
            # Retire le nombre premier choisi de l'ensemble
            prime_set.remove(prime)
            # Retire tous les multiples du nombre premier choisi
            multiples = set(range(prime, n + 1, prime))
            prime_set.difference_update(multiples)
            # Change de tour
            turn = 1 - turn

        # Le gagnant est celui dont c'était
        # le tour de jouer au dernier mouvement
        return "Maria" if turn == 1 else "Ben"

    # Compte le nombre de victoires pour Maria et Ben
    vmaria_wins = sum(playgame(num) == "Maria" for num in nums)
    vben_wins = x - vmaria_wins

    # Détermine le gagnant global
    # basé sur le nombre de victoires
    if vmaria_wins > vben_wins:
        return "Maria"
    elif vben_wins > vmaria_wins:
        return "Ben"
    else:
        # Retourne None en cas d'égalité
        return None
