"""
Du har blitt ansatt for å utvikle et program for et bibliotek som håndterer utlån av bøker. 
Biblioteket har både vanlige trykte bøker og elektroniske bøker (e-bøker). 
Hver bok har felles attributter som tittel, forfatter, utgivelsesår og en 
unik identifikasjonskode. E-bøker skiller seg ut ved å ha en unik nedlastingslenke 
i tillegg til de vanlige attributtene, og den har en utløpsdato etter 30 dager. Da låses boken.
Det finnes også en sjelden bok kalt "Diamond Sutra" fra Tang-dynastiet fra 
år 868 som kan lånes i biblioteket, men ikke tas med hjem. Den har et ekstra 
attributt som viser hvor den kan bli funnet i biblioteket.
"""

from random import randint

class Bibliotek:
    def __init__(self, navn, bøker=[]) -> None:
        self.navn = navn
        self.bøker = bøker
        self.utlån = []

    def registrerNyBok(self, bok):
        self.bøker.append(bok)

    def lånUt(self, bok):
        self.utlån.append(bok)
    
    def leverInn(self, bok):
        self.utlån.remove(bok)
    
    def visAlleBøker(self):
        print("---------------")
        print("Alle bøker")
        for bok in self.bøker:
            print(bok)
    
    def visAlleUtlån(self):
        print("---------------")
        print("Alle utlån")
        for bok in self.utlån:
            print(bok)

    def visAlleForfattere(self):
        print("---------------")
        print("Alle forfattere")
        buffer = []
        # Gå gjennom alle bøker og legg til forfatteren dersom den ikke forekommer i listen.
        for bok in self.bøker:
            if bok.forfatter not in buffer:
                buffer.append(bok.forfatter)
        for f in buffer:
            print(f)


class Bok:
    idTeller = 10000
    def __init__(self, tittel, forfatter, år, antSider) -> None:
        self.tittel = tittel
        self.forfatter = forfatter
        self.år = år
        self.isbn = self.setIsbn()
        self.type = "bok"
        self.antSider = antSider
    
    def setIsbn(self):
        Bok.idTeller += randint(100,500)
        return f"ISBN-{Bok.idTeller}"
    
    def __str__(self):
        return f"[{self.type}] {self.forfatter} - {self.tittel}, {self.år}, {self.antSider} sider - {self.isbn}"

class Ebok(Bok):    
    def __init__(self, tittel, forfatter, år, antSider) -> None:
        super().__init__(tittel, forfatter, år, antSider)
        self.lenke = f"https://{self.tittel}_{self.isbn}"
        self.utlånsdato = "2024-02-15"
        self.låst = False
        self.type = "ebok" 
    
    def sjekkUtløp(self):
        # 1) sjekk tid med datetime
        # 2) Finn timediff fra utslånsdato
        timediff = 15 # Hardkoder en verdi for testing
        if timediff > 30:
            self.låst = True
    
    def __str__(self):
        return super().__str__() + ", lenke: " + self.lenke

class DiamondSutra(Bok):
    def __init__(self) -> None:
        super().__init__("Diamond Sutra", "Tan-Dynastiet", 868, 250)
        self.lokasjon = "Hylle B28-5"
        self.type = "Ikke utlån"
        
    def __str__(self):
        return super().__str__() + ", Lokasjon: " + self.lokasjon



bok1 = Bok("Atomteori","Bohr, Nils",1958, 167)
bok2 = Bok("Relativitetsteorien","Albert Einstein",1916, 165)
bok3 = Ebok("Odyseen","Homer",2006, 541)

bib = Bibliotek("Nesodden bibliotek", [bok1, bok2, bok3])

bok4 = DiamondSutra()

bib.registrerNyBok(bok4)

bib.visAlleBøker()

print("-------------")

bib.visAlleForfattere()

bib.lånUt(bok1)
bib.visAlleUtlån()
bib.leverInn(bok1)
bib.visAlleUtlån()
