from Person import Person

class Laerer(Person):
    """
    Klasse for å lage lærer-objekter.
    Parametre:
    fornavn (str): Personens fornavn
    etternavn (str): Personens etternavn
    foedselsaar (int): Året personen ble født
    fag (list): Liste over fagene læreren kan undervise i
    kontaktklasse (str): Klassen læreren ev. er kontaktlærer for
    """
    def __init__(self, fornavn: str, etternavn: str, foedselsaar: int, fag:
        list, kontaktklasse: str = ""):
        super().__init__(fornavn, etternavn, foedselsaar)
        self.fag = fag
        self.kontaktklasse = kontaktklasse
    def sjekkfag(self, fagnavn: str):
        """ Metoden sjekker om læreren underviser i et gitt fag """
        return fagnavn in self.fag
    def visInfo(self, aarstall):
        """ Metoden skriver ut informasjon om læreren """
        super().visInfo(aarstall)
        if (len(self.fag) > 0):
            fagtekst = f"{self.fornavn} "
        if (self.kontaktklasse != ""):
            fagtekst += f"er kontaktlærer for {self.kontaktklasse} og "
            fagtekst += "underviser i "
            n = len(self.fag)
            for i in range(n):
                if (i == n-1):
                    fagtekst += " og "
                elif (i > 0):
                    fagtekst += ", "
                    fagtekst += f"{self.fag[i]}"
                    print(fagtekst)
# Test av Laerer-klassen
laerer1 = Laerer("Ola", "Nilsen", 1952, ["Matematikk", "Naturfag"], "8C")
laerer1.visInfo(2022)
print(laerer1.sjekkfag("Engelsk"))
print(laerer1.sjekkfag("Matematikk"))
laerer2 = Laerer("Gunvor", "Bjørk", 1970, ["Biologi", "Naturfag", "Tysk"])
laerer2.visInfo(2022)