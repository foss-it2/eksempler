"""
Klassevariabel:
Kan leses av alle objekter av klassen.
"""
class Youtube:
    brukerid = 1
    def __init__(self) -> None:
        self.brukere = []
    
    def leggTilBruker(self, bruker):
        bruker.id = Youtube.brukerid
        Youtube.brukerid += 1   # Her oppdateres klassevariabelen så den er én større for neste bruker.
        self.brukere.append(bruker)

class Bruker:
    def __init__(self, brukernavn) -> None:
        self.brukernavn = brukernavn
        self.videoer = []
        self.id = None

henrik = Bruker("hmauroy")
print(henrik.id)    # Printer None
youtube = Youtube()
youtube.leggTilBruker(henrik) # Nå vil henrik.id bli satt til et tall.
print(henrik.id)    # printer et eller annet tall som er gitt av Youtubes klassevariabel.
print(f"Youtubes klassevariabel er nå: {youtube.brukerid}")

