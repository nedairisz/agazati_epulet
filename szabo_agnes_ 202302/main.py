import bevezetes
import sorozat
import epuletek


# bevezetes.jatek()
dobasok = sorozat.listaba()
# print(dobasok)
sorozat.kiir(dobasok)
# print(sorozat.fejek_szama(dobasok))
db = sorozat.fejek_szama(dobasok)
sorozat.konzol_kiir(db)
sorozat.file_kiir(db)
lista = epuletek.listaba()
epuletek.kiiratas(lista)
print(epuletek.nagyobb(lista))
print(epuletek.legoregebb(lista))