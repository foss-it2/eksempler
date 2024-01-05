"""
Beskriver noen klasser.
"""

class Mobil:
    def __init__(self, merke):  # Metode
        self.merke = merke
        self.lengde = 100
        self.bredde = 70
        self.hoyde = 8
        self.underholdende = True
        self.ringbar = True

x10e = Mobil("Sony")

print(x10e.merke)

class Person:
    def __init__(self,fornavn, etternavn,alder):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.alder = alder
    
    def __str__(self):
        return f"{self.fornavn} {self.etternavn}, {self.alder} år"
    
    def hundeaar(self):
        hundeaar = self.alder * 7
        print(f"Jeg er {hundeaar} hundeår gammel. Det er skikkelig mye!")
    
# 1) Lag et Person-objekt.
# 2) Skriv ut alle attributtene til objektet
h = Person("henrik","m",3)
print(h)
# Endrer attributt
h.alder = 29
print(h)

h.hundeaar()

nr2 = Person("nr", "2",100)
nr3 = Person("nr", "TRE", 42)
# Legger folk i en liste
personer = []
personer.append(h)
personer.append(nr2)
personer.append(nr3)
for p in personer:
    print(p)    # NB! Printer objektet.

