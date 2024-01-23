"""
Private variabler kan ikke endres utenfra.
Objektene selv må endre dem.
"""

class Person:
    antallMennesker = 0
    def __init__(self,fornavn, etternavn, fnummer) -> None:
        self.fornavn = fornavn
        self.etternavn = etternavn
        self._fnummer = fnummer # Underscore betyr at variabelen er privat
        self._politiskParti = "SP"
        Person.antallMennesker += 1

    def getFnummer(self):
        return self._fnummer
    
    def getParti(self):
        passw = input("Hva er passordet? ")
        if passw == "passord":
            return self._politiskParti
        else:
            return None
    
    def setParti(self, parti):
        self._politiskParti = parti
    
person = Person("Navn", "Navnesen", 12345)
person.setParti("Rødt")
print(person.getParti())
