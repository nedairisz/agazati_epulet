"""
I/A:
Játékos neve: Gandalf
szerepkör: varázsló
I/B:
Üdvözlünk Gandalf, 2 életed van!

A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
    Játékos neve és szerepköre!  (2p)
B.	A program az adatbekérés után írasson ki egy üdvözlést az alábbiak alapján!
Amennyiben „varázsló” a játékosunk, 2 élete van.
Amennyiben „harcos” a játékosunk, 10 életereje van.
Amennyiben ismeretlen a játékosunk szerepköre, 8 életereje van. (4p)
"""

def bekeres():
    jatekos:str= str(input("Játékos neve: "))
    szerepkor:str= str(input("szerepkör: "))
    print("I/B:")
    if szerepkor=="varázsló":
        print("Üdvözlünk Gandalf, 2 életed van!")
    elif szerepkor=="harcos":
        print("Üdvözlünk harcos, 10 életed van!")
    else:
        print("Üdvözlünk, 8 életed van!")