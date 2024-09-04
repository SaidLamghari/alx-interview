#!/usr/bin/python3
"""
Jeu des Nombres Premiers
Auteur : SAID LAMGHARI
"""


def sieve_of_eratosthenes(max_n):
    """
    Génère une liste de nombres premiers jusqu'à max_n en utilisant le Crible d'Ératosthène.

    :param max_n: Limite supérieure pour la génération des nombres premiers.
    :return: Liste des nombres premiers jusqu'à max_n.
    """
    is_prime = [True] * (max_n + 1)  # Liste de booléens pour marquer les nombres premiers
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            # Marque les multiples de p comme non premiers
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    # Retourne la liste des nombres premiers
    return [p for p in range(2, max_n + 1) if is_prime[p]]

def calculate_grundy(n, primes):
    """
    Calcule le nombre de Grundy pour un nombre donné n en utilisant la liste des nombres premiers.

    :param n: Le nombre pour lequel le nombre de Grundy est calculé.
    :param primes: Liste des nombres premiers jusqu'à n.
    :return: Nombre de Grundy pour n.
    """
    grundy = [0] * (n + 1)  # Liste des nombres de Grundy pour chaque nombre jusqu'à n
    for i in range(1, n + 1):
        reachable = set()  # Ensemble des nombres de Grundy accessibles à partir de i
        for prime in primes:
            if prime > i:
                break
            reachable.add(grundy[i - prime])
        # Trouve le plus petit nombre de Grundy non présent dans l'ensemble reachable
        while grundy[i] in reachable:
            grundy[i] += 1
    return grundy[n]

def isWinner(x, nums):
    """
    Détermine le gagnant du jeu des nombres premiers après x tours.

    :param x: Nombre de tours.
    :param nums: Liste des valeurs de n pour chaque tour.
    :return: Nom du joueur ayant gagné le plus de tours ("Maria" ou "Ben"), ou None en cas d'égalité.
    """
    if x < 1 or not nums:
        return None  # Aucun tour ou liste vide

    max_n = max(nums)  # Trouve la valeur maximale dans nums pour optimiser la génération des nombres premiers
    primes = sieve_of_eratosthenes(max_n)  # Génère tous les nombres premiers jusqu'à max_n

    maria_wins = 0  # Compteur des victoires de Maria
    ben_wins = 0    # Compteur des victoires de Ben

    for n in nums:
        grundy_number = calculate_grundy(n, primes)  # Calcule le nombre de Grundy pour n
        # Le joueur Maria gagne si le nombre de Grundy est impair, sinon Ben gagne
        if grundy_number % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Détermine le gagnant global basé sur le nombre de victoires
    if maria_wins == ben_wins:
        return None  # Égalité
    return "Maria" if maria_wins > ben_wins else "Ben"

