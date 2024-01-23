class Person:
    """
    Klasse for å lage planet-objekter.
    Parametre:
    fornavn (str): Personens fornavn
    etternavn (str): Personens etternavn
    foedselsaar (int): Personens fødselsår
    """
    def __init__(self, fornavn, etternavn, foedselsaar):
        """ Konstruktør """
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.foedselsaar = foedselsaar
    
    def beregnAlder(self, aarstall):
        """ Metode som beregner personens alder """
        return aarstall - self.foedselsaar
    
    def visInfo(self, aarstall):
        """ Metode som skriver ut informasjon om personen """
        print(f"{self.fornavn} {self.etternavn} er {self.beregnAlder(aarstall)} år gammel.")