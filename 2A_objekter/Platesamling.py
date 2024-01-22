class Platesamling:
    def __init__(self, fornavn, liste=[]) -> None:
        self.eier = fornavn
        self.plater = liste # Liste med Albumobjekter

    def visAlbum(self):
        """Viser alle album"""
        for album in self.plater:
            print(album)

    def visArtister(self):
        teller = 1
        for album in self.plater:
            print(f"Artist {teller}: {album.artist}")
            teller += 1

    def leggTilAlbum(self, album):
        self.plater.append(album)


class Album:
    def __init__(self, artist, tittel, år) -> None:
        self.artist = artist
        self.tittel = tittel
        self.år = år
    
    def __str__(self):
        """Utskriftsfunksjon Album"""
        return f"Tittel: {self.tittel}, Artist: {self.artist}, Utgitt: {self.år}"

class Vinyl(Album):
    def __init__(self, artist, tittel, år, diameter=12) -> None:
        super().__init__(artist, tittel, år)
        self.diameter = diameter
    
    def beregnHastighet(self):
        """Returnerer hastigheten vinyl-albumet må spilles av på."""
        if self.diameter < 12:
            return "Høy"
        else:
            return "Lav"
    
    def __str__(self):
        """Utskriftsfunksjon Vinyl utvider superklassens utskrift med ekstra informasjon."""
        return super().__str__() + f", diameter: {self.diameter}, hastighet: {self.beregnHastighet()}."

class CD(Album):
    def __init__(self, artist, tittel, år, dobbeltsidig=False) -> None:
        super().__init__(artist, tittel, år)
        self.dobbeltsidig = dobbeltsidig
    
    def __str__(self):
        """Utskriftsfunksjon Vinyl utvider superklassens utskrift med ekstra informasjon."""
        if self.dobbeltsidig:
            return super().__str__() + ", dobbeltsidig."
        else:
            return super().__str__()


def main():
    fatOfTheLand = CD("Prodigy","Fat of the land",1997)
    sam = CD("Metallica", "Symphony and Metallica",1999,True)
    
    samling = Platesamling("Henrik",[fatOfTheLand,sam])
    samling.visAlbum()
    print("")

    home = Vinyl("Mhoo", "Home is where you are", 2013, 12)
    samling.leggTilAlbum(home)
    samling.visAlbum()
    print("")

    samling.visArtister()

if __name__ == "__main__":
    """Hvis denne filen er hovedprogrammet er denne if-testen True og vi kjører testprogrammet main()"""
    main()