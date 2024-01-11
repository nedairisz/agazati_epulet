class Epulet:
    def __init__(self, nev:str, varos:str, orszag:str, magassag:float, emelet:int, evszam:int):
        self.nev=nev
        self.varos=varos
        self.orszag=orszag
        self.magassag=magassag
        self.emelet=emelet
        self.evszam=evszam

#epulet1=Epulet("Avenue", "17 block", "Moszkav", "Oroszország", 155, 43, 2008)  ez a self