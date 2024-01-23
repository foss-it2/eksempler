"""
Implementering av et UML-diagram.
"""

class Youtube:
    def __init__(self, initialUsers=[]) -> None:
        self.brukere = initialUsers
    
    def leggTilBruker(self, bruker):
        self.brukere.append(bruker)
    

class Bruker:
    def __init__(self, brukernavn) -> None:
        self.brukernavn = brukernavn
        self.videoer = []
    
    def leggTilVideo(self, video):
        self.videoer.append(video)

class Admin(Bruker):
    def __init__(self, brukernavn) -> None:
        super().__init__(brukernavn)

    def slettVideo(self, bruker, videoobjekt):
        # Algoritme som søker etter objektet videoobjekt i listen til en bruker.
        # Ikke tid til å skrive den på denne vurderingen.
        pass

class Video:
    def __init__(self, tittel, lengde) -> None:
        self.tittel = tittel
        self.lengde = lengde
        self.likes = 0
    
    def leggTilLike(self):
        self.likes += 1