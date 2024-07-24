#!/usr/bin/python3
"""
Write a method that determines if a
given data set represents a valid UTF-8 encoding.
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
    # Count of remaining bytes to process for current UTF-8 character
    ring_bytes = 0
    
    for nm in data:
        # Check the most significant bits to determine the type of UTF-8 character
        if ring_bytes == 0:
            if (nm >> 3) == 0b11110:
                ring_bytes = 3
            elif (nm >> 4) == 0b1110:
                ring_bytes = 2
            elif (nm >> 5) == 0b110:
                ring_bytes = 1
            elif (nm >> 7):
                return False
        else:
            # If current byte does not start with 10,
            # it's not a valid continuation byte
            if (nm >> 6) != 0b10:
                return False
            ring_bytes -= 1
    
    # If we have remaining bytes
    # after processing all integers, it's invalid
    return ring_bytes == 0
