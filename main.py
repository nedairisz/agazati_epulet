import bevezetes
import sorozat
import epuletek

"""
print("I/A:")
bevezetes.bekeres()
print()

print("II/A, B, C:")
lista=sorozat.dobasok()
print("\nII/D, E:")
szamlalo=sorozat.fejek_szama(lista)
sorozat.konzol_kiir(szamlalo)
print("II/F:")
sorozat.file_kiir(szamlalo)
print(f"\tA fejek száma: {szamlalo}")
print()
print()"""

print("III/A, B:")
lista=epuletek.beolvas()
szamlalo=epuletek.epuletek_szama(lista)
print(f"\tAz épületek száma: {szamlalo}")
print("III/C:")
gyujto=epuletek.magasabb(lista)
print(f"\tAz 555 lábnál magasabb épületek száma: {gyujto}")
print("III/D:")
legoregebb=epuletek.legoregebb(lista)
print(f"\tA legöregebb épület országa: {legoregebb}")