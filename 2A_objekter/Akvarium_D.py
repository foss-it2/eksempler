""""
Klasser som omhandler akvarium og fisker.
"""
from random import randint


class Akvarium:
    def __init__(self, l, b, h, fisker=[]) -> None:
        self.l = l
        self.b = b
        self.h = h
        self.fisker = fisker

    def beregnVolum(self):
        return (self.l * self.b * self.h) / 1000

    def vannVolum(self):
        # 1) beregne 90 % av høyden.
        # 2) beregne volum basert på maksimalhøyde.
        makshøyde = self.h * 0.9
        return self.l * self.b * makshøyde

    def vannHøyde(self, volum):
        # Volum er gitt i L: må da gange med 1000 for å få det over i cm^3.
        # Returnere vannhøyden ved gitt volum
        return 1000 * volum / (self.l * self.b)

    def leggTilFisk(self, fisk):
        if fisk.lengde >= 0.3*self.l:
            print(
                f"For kort akvarium for {fisk.navn}. Prøv med en lengde på minimum {fisk.lengde*3} cm")
        elif fisk.lengde >= 0.3*self.b:
            print(
                f"For smalt akvarium for {fisk.navn}. Prøv med en bredde på minimum {fisk.lengde*3} cm")
        elif fisk.lengde >= 0.3*self.h:
            print(
                f"For lavt akvarium for {fisk.navn}. Prøv med en høyde på minimum {fisk.lengde*3} cm")
        else:
            self.fisker.append(fisk)
            print(
                f"{fisk.navn} lagt oppi akvariet. Nå er det {len(self.fisker)} oppi akvariet.")


class Fisk:
    def __init__(self, navn, lengde, vekt) -> None:
        self.navn = navn
        self.lengde = lengde
        self.vekt = vekt

    def spis(self):
        # Endret til retur så den kan brukes av underklasser.
        return f"{self.navn} liker å spise"


class Hvithai(Fisk):
    def __init__(self, navn, lengde, vekt) -> None:
        super().__init__(navn, lengde, vekt)
        self.vitenskapelignavn = "Carcharodon carcharias"
        self.favorittmat = "sel"

    def hoppe(self):
        # Returnere 1/0 om den fanget en sel
        return randint(0, 1)

    def spis(self):
        tekst = super().spis() + f" {self.favorittmat}!"
        return tekst


class Rognkjeks(Fisk):
    def __init__(self, navn, lengde, vekt) -> None:
        super().__init__(navn, lengde, vekt)
        self.vitenskapelignavn = "Cyclopterus lumpus"
        self.favorittmat = "lakselus"
        self.sugdFast = False

    def sugFast(self):
        # Returnere true/false om den fanget en sel
        self.sugdFast = not self.sugdFast  # Flipper variabelen.
        return self.sugdFast

    def spis(self):
        tekst = super().spis() + f" {self.favorittmat}!"
        return tekst


def main():
    # Kjører programmet som hovedprogram.
    akv1 = Akvarium(10, 20, 15)
    print(f"Volum av tomt akvarium {akv1.beregnVolum():.1f} L")
    print(f"Volum av maksfylt akvarium {akv1.vannVolum():.1f} cm^3")
    print(f"2 liter vann når opp i høyde {akv1.vannHøyde(2):.1f} cm")

    # Lager en fisk.
    torsk = Fisk("Torsk", 34, 0.4)
    print(torsk.spis())    # Kaller på metoden spis().
    kampfisk = Fisk("Kampfisk", 5, 0.010)
    print(kampfisk.spis())

    # oppg 2
    haiulf = Hvithai("hvithai", 400, 2000)
    print(haiulf.spis())
    print(f"Klarte haiulf å fange selen (1=ja, 0=nei)? {haiulf.hoppe()}")
    nemo = Rognkjeks("rognkjeks", 55, 5)
    print(f"Nemo er sugd fast: {nemo.sugFast()}")
    print(f"Nemo er sugd fast: {nemo.sugFast()}")

    # Oppg 3b/c
    akv2 = Akvarium(150, 100, 80, [nemo])
    akv2.leggTilFisk(haiulf)


if __name__ == "__main__":
    # If-testen sjekker om skriptet er selve hovedprogrammet.
    main()
