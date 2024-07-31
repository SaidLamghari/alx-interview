#!/usr/bin/python3
"""
0x05. N Queens
Auteur SAID LAMGHARI
"""
import sys


def print_usage_exit():
    """
    Affiche le message d'utilisation et quitte
    le programme avec le statut 1.
    """
    print("Usage: nqueens N")
    sys.exit(1)


def print_errr_exit(message):
    """
    Affiche un message d'erreur spécifique et
    quitte le programme avec le statut 1.

    :param message: Message d'erreur à afficher
    """
    print(message)
    sys.exit(1)


def is_safe(board, row, col, N):
    """
    Vérifie si il est sûr de placer une reine à la position (row, col).

    :param board: Liste représentant la position des reines sur le plateau
    :param row: Ligne actuelle où on souhaite placer la reine
    :param col: Colonne actuelle où on souhaite placer la reine
    :param N: Taille du plateau (N x N)
    :return: True si il est sûr de placer la reine, False sinon
    """
    # Vérifie la colonne
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def slve_nqueensutil(board, row, N):
    """
    Fonction récursive pour résoudre le problème
    des N reines en utilisant le retour arrière.

    :param board: Liste représentant la position des reines sur le plateau
    :param row: Ligne actuelle où on souhaite placer la reine
    :param N: Taille du plateau (N x N)
    """
    if row == N:
        # Lorsque toutes les reines sont placées, imprime la solution
        solution = [[i, board[i]] for i in range(N)]
        print(solution)
        return

    # Essayez de placer une reine dans chaque colonne de la ligne actuelle
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            # Appel récursif pour essayer de placer les autres reines
            slve_nqueensutil(board, row + 1, N)
            # Retire la reine de la position actuelle (retour arrière)
            board[row] = -1


def solve_nqueens(N):
    """
    Initialise le plateau et commence à résoudre le problème des N reines.

    :param N: Taille du plateau (N x N)
    """
    board = [-1] * N  # Initialisation duplateau avec -1 (aucune reine placée)
    slve_nqueensutil(board, 0, N)


def main():
    """
    Fonction principale pour gérer les arguments
    de ligne de commande et lancer la résolution.
    """
    # Vérifie que le bon nombre d'arguments est fourni
    if len(sys.argv) != 2:
        print_usage_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_errr_exit("N must be a number")

    # Vérifie que N est un nombre entier supérieur ou égal à 4
    if N < 4:
        print_errr_exit("N must be at least 4")

    # Lance la résolution du problème des N reines
    solve_nqueens(N)


if __name__ == "__main__":
    main()
