import random
import os
import string

def aanslagnummer():
    cijfers = ''.join(random.choices(string.digits, k=7))
    aanslagnummer = '000' + cijfers
    return aanslagnummer

def kentekens():
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    cijfers = ''.join(random.choices(string.digits, k=3))
    letter = random.choice(string.ascii_uppercase)
    kenteken = letters + cijfers + letter
    return kenteken


def automerken():
    locatie = "templates/automerken.txt"
    if not os.path.exists(locatie):
        return "Bestand niet gevonden op " + locatie

    with open("templates/automerken.txt", 'r') as file:
        automerken = [line.strip() for line in file.readlines()]
        automerken = [automerk[:20].ljust(20) for automerk in automerken]
        return random.choice(automerken)


def kleuren():
    locatie = "templates/kleuren.txt"
    if not os.path.exists(locatie):
        return "Bestand niet gevonden op " + locatie

    with open("templates/kleuren.txt", 'r') as file:
        kleuren = [line.strip() for line in file.readlines()]
        kleuren = [kleur[:6].ljust(6) for kleur in kleuren]
        return random.choice(kleuren)


def straatnamen():
    locatie = "templates/straatnamen.txt"
    if not os.path.exists(locatie):
        return "Bestand niet gevonden op " + locatie

    with open("templates/straatnamen.txt", 'r') as file:
        straatnamen = [line.strip() for line in file.readlines()]
        straatnamen = [straat[:25].ljust(25) for straat in straatnamen]
        return random.choice(straatnamen)
