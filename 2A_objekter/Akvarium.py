class Akvarium:
    def __init__(self,l,b,h) -> None:
        self.l = l
        self.b = b
        self.h = h
    
    def beregnVolum(self):
        return (self.l * self.b * self.h) / 1000
    
    def vannVolum(self):
        # 1) beregne 90 % av høyden.
        # 2) beregne volum basert på maksimalhøyde.
        makshøyde = self.h * 0.9
        return self.l * self.b * makshøyde

    def vannHøyde(self,volum):
        # Volum er gitt i L: må da gange med 1000 for å få det over i cm^2.
        # Returnere vannhøyden ved gitt volum
        return 1000 * volum / (self.l * self.b)

class Fisk:
    def __init__(self, navn) -> None:
        self.navn = navn
    
    def spis(self):
        print(f"{self.navn} liker å spise")

class Hvithai(Fisk):
    def __init__(self, navn) -> None:
        super().__init__(navn)
        self.vitenskapelignavn = "Carcharodon carcharias"
        self.lengde = 4000 # cm
        self.vekt = 2000    # kg
        self.favorittmat = "sel"
    
    def hoppe(self):
        # Returnere true/false om den fanget en sel
        pass

def main():
    # Kjører programmet som hovedprogram.
    akv1 = Akvarium(10,20,15)
    print(f"Volum av tomt akvarium {akv1.beregnVolum():.1f} L")
    print(f"Volum av maksfylt akvarium {akv1.vannVolum():.1f} cm^3")
    print(f"2 liter vann når opp i høyde {akv1.vannHøyde(2):.1f} cm")

    # Lager en fisk.
    torsk = Fisk("Torsk")
    torsk.spis()    # Kaller på metoden spis().
    kampfisk = Fisk("Kampfisk")
    kampfisk.spis()

if __name__ == "__main__":
    # If-testen sjekker om skriptet er selve hovedprogrammet.
    main()