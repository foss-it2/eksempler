class Platesamling:
    def __init__(self, fornavn, liste=[]) -> None:
        self.eier = fornavn
        self.plater = liste # Liste med Albumobjekter

    def visAlbum(self):
        pass

    def visArtister(self):
        pass

    def leggTilAlbum(self, album):
        self.plater.append(album)


class Album:
    def __init__(self, artist, tittel, år=-5000) -> None:
        self.artist = artist
        self.tittel = tittel
        self.år = år

class Vinyl(Album):
    def __init__(self, artist, tittel, diameter=12, år=1958) -> None:
        super().__init__(artist, tittel, år)
        self.diameter = diameter
    
    def beregnHastighet(self):
        if self.diameter < 12:
            return "Høy"
        else:
            return "Lav"

class CD(Album):
    def __init__(self, artist, tittel, dobbeltsidig=False, år=1986) -> None:
        super().__init__(artist, tittel, år)
        self.dobbeltsidig = dobbeltsidig
