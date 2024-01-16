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

def main():
    # Kjører programmet som hovedprogram.
    akv1 = Akvarium(10,20,15)
    print(f"Volum av tomt akvarium{akv1.beregnVolum():.1f}")
    print(f"Volum av maksfylt akvarium {akv1.vannVolum():.1f}")
    print(f"2 liter vann når opp i høyde{akv1.vannHøyde(2):.1f} cm")

if __name__ == "__main__":
    # If-testen sjekker om skriptet er selve hovedprogrammet.
    main()