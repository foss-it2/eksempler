"""

"""
from random import randint

tabell = []
for i in range(10):
    rad = []
    for j in range(10):
        rad.append(False)
    tabell.append(rad)

# Velger tilfeldig 5 ulike indekser som settes lik True
# NB! Samme plass i 2D-listen kan velges flere ganger.
for i in range(5):
    rad = randint(0,9)
    kol = randint(0,9)
    tabell[rad][kol] = True

for rad in tabell:
    print(rad)

# Lager en ny tabell som endres på en smartere måte.
tabell2 = []
for i in range(10):
    rad = []
    for j in range(10):
        rad.append(False)
    tabell2.append(rad)

indekser_valgt = []
while len(indekser_valgt) < 5:
    rad = randint(0,9)
    kol = randint(0,9)
    if tabell2[rad][kol] == False:
        tabell2[rad][kol] = True
        indekser_valgt.append([rad,kol])
print("*"*100)
for rad in tabell2:
    print(rad)