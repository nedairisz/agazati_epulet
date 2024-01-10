import random

# listába tesszük
def listaba():
    dobasok = []
    for i in range(7):
        # balról zárt, jobbról nyitott
        dobas = random.randrange(0, 2)
        dobasok.append(dobas)
    return dobasok


def kiir(lista):
    print("II/A, B, C:", end="\n\t")
    for i in range(len(lista)-1):
        if lista[i]:
            print("FEJ", end="-")
        else:
            print("ÍRÁS", end="-")
    if lista[-1]:
        print("FEJ")
    else:
        print("ÍRÁS")


def fejek_szama(lista):
    db = 0
    for i in range(len(lista)):
        if lista[i]:
            db += 1
    return db


def konzol_kiir(db: int):
    print(f"II/D, E:\n\tA fejek száma: {db}.")


def file_kiir(db: int):
    f = open("fejek.txt", "w", encoding="utf8")
    f.write(f"II/F:\n\tA fejek száma: {db}.")
    f.close()

