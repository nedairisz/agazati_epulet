"""
Az epulet.txt forrásállomány, épületek adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Az epulet.txt állomány szerkezete:
·         az épület neve: pl: Centrum LIM
·         az épület városa: pl.: Varsó
·         az épület országa: pl.: Lengyelország
·         az épület magassága m-ben: pl.: 140
·         az épület emeleteinek a száma, pl.: 43
⦁	      az épület építésének az éve, pl.1949
Az állomány első sora a mezőneveket tartalmazza „$” jellel elválasztva.

III/A, B:
            	Az épületek száma: 8
III/C:
            	Az 555 lábnál magasabb épületek száma: 2.
III/D:
            	A legöregebb épület országa: Lengyelország.            	
⦁	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) 
    a epulet.txt fájlból a játékosok adatait, és tárolja el összetett 
    adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! 
    Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
⦁	Írassa ki az épületek számát a mintának megfelelően a konzolra! (2p)
⦁	Adja meg az 555 lábnál magasabb épületek számát, ha 1 m = 3.280839895 láb! (4p)
⦁	Írassa ki konzolra a mintának megfelelően a legöregebb épület 
    (ha több is van, akkor az első legöregebb adatait) országát. (4p)
"""
from Epulet import Epulet

def beolvas():
    fajl=open("epulet.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close

    lista=[]
    for i in range(0, len(nyers_lista), 1):
        sorok=nyers_lista[i]
        egy_sor=sorok.strip().split("$")
        nev:str=(egy_sor[0])
        varos:str=(egy_sor[1])
        orszag:str=(egy_sor[2])
        magassag:int=(egy_sor[3])
        emelet:int=(egy_sor[4])
        evszam:int=(egy_sor[5])
        epulet=Epulet(nev, varos, orszag, magassag, emelet, evszam)
        lista.append(epulet)

    return lista

def epuletek_szama(lista):
    szamlalo:int=0
    for i in range(0, len(lista), 1):
        szamlalo+=1
    return szamlalo

def magasabb(lista):
    gyujto:int =0
    meret:int= 500/3.280839895
    for i in range(0, len(lista), 1):
        epulet_meret= float(lista[i].magassag.replace(",", "."))
        if epulet_meret > meret:
            gyujto+=1
    return gyujto

def legoregebb_epulet(lista):
    legoregebb=3000
    legoregebb_index=0
    for i in range(0, len(lista), 1):
        if legoregebb < lista[i].evszam:
            legoregebb=lista[i].evszam
            legoregebb_index=i
    return lista[legoregebb_index].orszag