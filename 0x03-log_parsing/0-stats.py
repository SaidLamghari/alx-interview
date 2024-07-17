#!/usr/bin/python3
import sys
import signal
import re

# Variables globales
ttl_size = 0  # Taille totale des fichiers
status_cds = {
    200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
}  # Comptage des codes de statut
line_cnt = 0  # Compteur de lignes

# Expression régulière pour correspondre au format de log
log_rgx = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>.+)\] '
    r'"GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)'
)


def print_stts():
    """Affiche les statistiques actuelles."""
    print(f"File size: {ttl_size}")
    for code in sorted(status_cds.keys()):
        if status_cds[code] > 0:
            print(f"{code}: {status_cds[code]}")


def handle_intrrpt(signum, frame):
    """Gère l'interruption du clavier (CTRL + C)."""
    print_stts()
    sys.exit(0)


# Enregistre le gestionnaire de
# signaux pour les interruptions du clavier
signal.signal(signal.SIGINT, handle_intrrpt)

try:
    for line in sys.stdin:
        line_cnt += 1
        match = log_rgx.match(line)
        if match:
            data = match.groupdict()
            # Ajoute la taille du fichier à la taille totale
            ttl_size += int(data['size'])
            status_code = int(data['status'])
            if status_code in status_cds:
                # Incrémente le compteur du code de statut
                status_cds[status_code] += 1

        if line_cnt % 10 == 0:
            # Affiche les statistiques après chaque 10 lignes
            print_stts()

except Exception:
    pass

# Affiche les statistiques finales à la fin de la lecture
print_stts()
