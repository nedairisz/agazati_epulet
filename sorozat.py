"""
II/A, B, C:
           	FEJ-ÍRÁS-ÍRÁS-ÍRÁS-FEJ-ÍRÁS-ÍRÁS
II/D, E:
           	A fejek száma: 2.  	
            A fejek.txt tartalma:
II/F:
            A fejek száma: 2. 	
 
⦁	Írasson ki a konzolra kötőjellel (-) elválasztva 7 pénzérmével való dobást 
    véletlen számsorozat alapján a mintának megfelelően! (4p)
⦁	A generált értékeket tárolja lista adatszerkezetben logikai típusokkal 
    (0: írás, 1: fej)! (1p)
⦁	A „–” jel csak az értékek között szerepeljen (a végén ne)! (2p)
⦁	Írjon függvényt fejek_szama néven, amiben számolja meg, hogy hány olyan 
    elem van, ami fej (1). A visszatérési érték legyen egy egész szám! (3p)
⦁	A fejek_szama függvény eredményét írassa ki a mintának megfelelően a konzolra, 
    amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
⦁	A fejek_szama függvény eredményét írassa ki a mintának megfelelően a 
    fejek.txt nevű fájlba, amit file_kiir nevű metódusban fogalmazzon meg! (2p)
"""

import random

def dobasok():
    lista=[]
    for i in range(0, 7, 1):
        dobas=random.randint(0,1)
        lista.append(dobas)

        if dobas==0:
            if i==6:
                print("ÍRÁS", end="")
            else:
                print("ÍRÁS", end="-")
        elif dobas==1:
            if i ==6:
                print("FEJ", end="")
            else:
                print("FEJ", end="-")

    return lista

def fejek_szama(lista):
    szamlalo=0
    for i in range(len(lista)):
        if lista[i] == 1:
            szamlalo+=1
    return szamlalo

def konzol_kiir(szamlalo):
    print(f"A fejek száma: {szamlalo}")

def file_kiir(szamlalo):
    fajl=open("fejek.txt", "w", encoding="utf-8")
    fajl.write(f"A fejek száma: {szamlalo}")
    fajl.close()