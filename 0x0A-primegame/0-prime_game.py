#!/usr/bin/python3
"""Module de jeu des nombres premiers.
auteur SAID LAMGHARI
"""


def valsieve(max_num):
    """Génère une liste de nombres premiers jusqu'à
    max_num en utilisant le Crible d'Ératosthène.

    Args:
        max_num (int): La valeur maximale jusqu'à
        laquelle générer les nombres premiers.

    Returns:
        List[int]: Une liste contenant tous
        les nombres premiers jusqu'à max_num.
    """
    # Si max_num est inférieur à 2, il n'y
    # a pas de nombres premiers possibles
    if max_num < 2:
        return []

    # Crée une liste de booléens, où True signifie que
    # le nombre à cet index est considéré comme premier
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 et 1 ne sont pas des nombres premiers

    # Application du Crible d'Ératosthène
    p = 2
    while p * p <= max_num:
        if primes[p]:
            # Marque les multiples de p comme
            # non premiers, à partir de p*p
            for multiple in range(p * p, max_num + 1, p):
                primes[multiple] = False
        p += 1

    # Retourne la liste des nombres premiers
    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """Détermine le gagnant de chaque partie du jeu des nombres
    premiers et retourne le joueur qui a gagné le plus de parties.

    Args:
        x (int): Le nombre de parties.
        nums (List[int]): Liste des valeurs n pour chaque partie.

    Returns:
        str ou None: Le nom du joueur qui a gagné le plus de
        parties ('Maria' ou 'Ben'), ou None en cas d'égalité.
    """
    # Vérifie si le nombre de parties est valide
    # et que la liste des nombres n'est pas vide
    if x <= 0 or not nums:
        return None

    # Trouve la valeur maximale de n pour déterminer
    # jusqu'où générer les nombres premiers
    max_n = max(nums)

    # Génére la liste des nombres premiers jusqu'à max_n
    primes_list = valsieve(max_n)

    # Convertit la liste des nombres premiers en
    # un ensemble pour des vérifications plus rapides
    prime_set = set(primes_list)

    # Initialise les compteurs de victoires pour Maria et Ben
    mariawns = 0
    benwns = 0

    # Parcourt chaque valeur n dans la liste nums pour chaque partie
    for n in nums:
        # Si n est inférieur à 2, il n'y a pas de nombres
        # premiers à choisir, donc Ben gagne automatiquement
        if n < 2:
            benwns += 1
            continue

        # Trouve tous les nombres premiers jusqu'à n
        primes_in_round = [p for p in primes_list if p <= n]

        # Détermine le gagnant basé sur le nombre
        # de nombres premiers disponibles
        if len(primes_in_round) % 2 == 1:
            # Si le nombre de nombres premiers est
            # impair, Maria gagne car elle joue en premier
            mariawns += 1
        else:
            # Si le nombre de nombres
            # premiers est pair, Ben gagne
            benwns += 1

    # Compare le nombre de victoires pour Maria et Ben
    if mariawns > benwns:
        return "Maria"
    elif benwns > mariawns:
        return "Ben"
    else:
        # En cas d'égalité, il n'y a pas de
        # gagnant clairement déterminé
        return None
