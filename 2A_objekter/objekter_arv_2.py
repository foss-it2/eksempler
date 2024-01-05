class Planet:
    def __init__(self, navn):
        self.navn = navn
    
    def visInfo(self):
        print(f"{self.navn}")

class Jorda(Planet):
    def __init__(self, navn):
        super().__init__(navn) # MÅ å ha med for arven!
        self.harLiv = True
        self.vannVolum = 1e25
        self.temperatur = 15.5

    def økTemperatur(self):
        self.temperatur += 0.25
    
# Superklasser
# Rom
class Rom:
    def __init__(self,romnr) -> None:
        self.romnr = romnr
        self.ledig = True
    
    def erLedig(self):
        return self.ledig
    
    def bookRom(self):
        self.ledig = False
    
    def sjekkUt(self):
        self.ledig = True
    

# Produkt
class Produkt:
    def __init__(self, id, antall) -> None:
        self.id = id
        self.antall = antall
    
    def getAntall(self):
        return self.antall

kopp = Produkt(492,57)
print(f"produkt nr. {kopp.id}: {kopp.getAntall()} stk.")


    


# Konto
class Konto:
    def __init__(self, kontonummer, innskudd) -> None:
        self.kontonummer = kontonummer
        self.saldo = innskudd
    
    def visSaldo(self):
        print(f"Saldo: {self.saldo}")

class Sparekonto(Konto):
    def __init__(self, kontonummer, innskudd, rente) -> None:
        super().__init__(kontonummer, innskudd)
        self.rente = rente
        self.uttakIgjen = 12

    def tarUtPenger(self):
        self.uttakIgjen -= 1
        if self.uttakIgjen < 0:
            print("Du har ingen uttak igjen!")
    

brukskonto = Konto(1357, 700)
brukskonto.visSaldo()