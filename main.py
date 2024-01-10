import bevezetes
import sorozat
import epuletek

"""
print("I/A:")
bevezetes.bekeres()

print("II/A, B, C:")
lista=sorozat.dobasok()
print("\nII/D, E:")
szamlalo=sorozat.fejek_szama(lista)
sorozat.konzol_kiir(szamlalo)
print("A fejek.txt tartalma:")
print("II/F:")
sorozat.file_kiir(szamlalo)"""

print("III/A, B:")
lista=epuletek.beolvas()
szamlalo=epuletek.epuletek_szama(lista)
print(f"Az épületek száma: {szamlalo}")
print("III/C:")
gyujto=epuletek.magasabb(lista)
print(f"Az 555 lábnál magasabb épületek száma: {gyujto}")
print("III/D:")
legoregebb=epuletek.legoregebb(lista)
print(f"A legöregebb épület országa: {legoregebb}")