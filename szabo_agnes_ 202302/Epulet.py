# név$város$ország$magasság(m)$emelet$épült
class Epulet:
    # konstruktor init!
    def __init__(self, sor: str):
        # tisztítás, darabolás, listába tétel
        adatok = sor.strip().split("$")
        self.nev = adatok[0]
        self.varos = adatok[1]
        self.orszag = adatok[2]
        self.magassag = float(adatok[3].replace(',', '.'))
        self.emelet = int(adatok[4])
        self.ev = int(adatok[5])
