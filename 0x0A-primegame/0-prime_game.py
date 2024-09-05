#!/usr/bin/python3
"""Module de jeu des nombres premiers.
auteur SAID LAMGHARI
"""


def sieve_of_eratosthenes(max_num):
    """Génère une liste de nombres premiers jusqu'à
    max_num en utilisant le Crible d'Ératosthène."""
    # Crée une liste de booléens initialisée à True.
    # Chaque index représente un nombre de 0 à max_num,
    # initialement considéré comme premier.
    primes = [True] * (max_num + 1)

    # Les nombres 0 et 1 ne sont pas premiers
    primes[0] = primes[1] = False

    # Démarre à partir du premier nombre premier, qui est 2
    p = 2
    # Continue tant que le carré de
    # p est inférieur ou égal à max_num
    while p * p <= max_num:
        # Si p est encore marqué comme premier
        if primes[p]:
            # Commence à marquer les multiples de p
            # comme non premiers, à partir de p*p
            multiple = p * p
            while multiple <= max_num:
                primes[multiple] = False
                multiple += p
        # Passe au nombre suivant
        p += 1
    return primes


def isWinner(x, nums):
    """Détermine le gagnant d'une session de
    jeu des nombres premiers avec `x` tours."""
    # Vérifie si le nombre de tours est valide et
    # si la liste des nombres n'est pas vide
    if x < 1 or not nums:
        return None

    # Trouve la valeur maximale dans la liste nums pour
    # déterminer jusqu'où générer les nombres premiers
    max_value = max(nums)
    # Génére une liste des nombres
    # premiers jusqu'à max_value
    primes = sieve_of_eratosthenes(max_value)

    # Initialise les compteurs
    # de victoires pour Maria et Ben
    mariaswns = benswns = 0
    # Compteur pour itérer sur les tours
    count = 0

    # Tant que nous avons des tours à traiter
    while count < x:
        # Obtient le nombre maximal pour le tour actuel
        n = nums[count]
        # Compte combien de nombres jusqu'à n sont premiers
        prime_count = sum(primes[:n])
        # Détermine le gagnant du tour basé sur
        # la parité du nombre de nombres premiers
        if prime_count % 2 == 0:
            # Si le nombre de nombres premiers
            # est pair, Ben gagne ce tour
            benswns += 1
        else:
            # Si le nombre de nombres premiers
            # est impair, Maria gagne ce tour
            mariaswns += 1
        # Passe au tour suivant
        count += 1

    # Utilise un dictionnaire pour
    # comparer les victoires de Maria et Ben
    winners = {'Maria': mariaswns, 'Ben': benswns}

    # Si le nombre de victoires
    # est égal, il n'y a pas de gagnant
    if mariaswns == benswns:
        return None

    # Retourne le nom du
    # joueur avec le plus de victoires
    return max(winners, key=winners.get)
