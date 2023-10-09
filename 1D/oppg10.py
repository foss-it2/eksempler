"""
byer = ["OSLOO", "Trondheim", "Bergen", "Stavaangir", "Kristiansand", "Drammen", "Tromsø"] . 
Byene er sortert etter synkende innbyggertall. Her er byene Stavanger og Oslo feilregistrert.
a Fjern verdien "Stavaangir" ved å bruke remove() .
b Fjern verdien "OSLOO" ved å bruke index() for å finne indeksen og pop() for å fjerne verdien.
c Legg til de riktige verdiene "Stavanger" og "Oslo" på de samme posisjonene der de feilstavede byene var.
"""

byer = ["OSLOO", "Trondheim", "Bergen", "Stavaangir", "Kristiansand", "Drammen", "Tromsø"]
byer.remove("Stavaangir")

oslo = byer.index("OSLOO")
byer.pop(oslo)

byer.insert(0,"Oslo")

indeks = byer.index("Bergen")
byer.insert(indeks + 1, "Stavanger")

print(byer)


