'''
Oppgave 10 - Livssyklus
IT-2 Eksamen Vår 2024
Antagelser:
    Celler på utsiden av rutenettet er døde.
Beskrivelse:
    Se oppgaveteksten.
Utgangspunkt:
    Pygame-mal fra Smidig IT-2
'''
import pygame as pg
from random import random

# Konstanter
MENY_HØYDE = 75
MARG = 25
RADER = 20
KOLONNER = 20
CELLE_STØRRELSE = 25
BREDDE = 2 * MARG + KOLONNER * CELLE_STØRRELSE
HØYDE = MENY_HØYDE + 2 * MARG + RADER * CELLE_STØRRELSE
FPS = 25

"""En celle har en tilstand (levende eller død) og en posisjon i rutenettet."""


class Celle(pg.sprite.Sprite):

    def __init__(self, rad, kolonne):
        super().__init__()
        self.rad = rad
        self.kolonne = kolonne
        self.er_død = True
        self.neste_tilstand = None
        self.image = pg.Surface((CELLE_STØRRELSE, CELLE_STØRRELSE))
        self.rect = self.image.get_rect()
        self.image.fill("white")
        self.rect.topleft = (MARG + kolonne * CELLE_STØRRELSE,
                             MENY_HØYDE + MARG + rad * CELLE_STØRRELSE)
        pg.draw.rect(self.image, "black", self.rect, 1)

    def update(self):
        '''Døde celler er hvite, og levende celler er svarte.'''
        farge = 'white' if self.er_død else 'black'
        self.image.fill(farge)
        rect = self.image.get_rect()
        pg.draw.rect(self.image, "black", rect, 1)

    def finn_naboceller(self, alle_celler):
        """Bruk rad og kolonne til å finne nabocellene til en celle."""
        self.naboceller = []
        for celle in alle_celler:
            if celle != self and abs(celle.rad - self.rad) <= 1 and abs(celle.kolonne - self.kolonne) <= 1:
                self.naboceller.append(celle)

    def beregn_neste_tilstand(self):
        '''Beregn neste tilstand for en celle basert på nabocellenes tilstand'''
        antall_levende_naboer = sum(
            not nabo.er_død for nabo in self.naboceller)
        if self.er_død:
            self.neste_tilstand = antall_levende_naboer != 3
        else:
            self.neste_tilstand = antall_levende_naboer not in (2, 3)


class App:
    def __init__(self):
        '''Initialiser pygame og opprett rutenettet med celler.'''
        pg.init()
        self.klokke = pg.time.Clock()
        self.skjerm = pg.display.set_mode((BREDDE, HØYDE))
        pg.display.set_caption("Livssyklus")
        self.alle_celler = pg.sprite.Group()
        for rad in range(RADER):
            for kolonne in range(KOLONNER):
                celle = Celle(rad, kolonne)
                self.alle_celler.add(celle)
        for celle in self.alle_celler:
            celle.finn_naboceller(self.alle_celler)
        self.kjører = True

    def behandle_hendelser(self):
        """Behandle brukerinput fra tastatur og mus."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.kjører = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_s:
                    self.start()
                elif event.key == pg.K_t:
                    self.tøm()
                elif event.key == pg.K_n:
                    self.neste_generasjon()
            # Klikk på celle for å endre tilstand
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                for celle in self.alle_celler:
                    if celle.rect.collidepoint(pos):
                        celle.er_død = not celle.er_død

    def oppdater(self):
        """Oppdater alle cellene i rutenettet."""
        self.alle_celler.update()

    def tegn(self):
        """Tegn hele spillet med meny og rutenett på skjermen."""
        self.skjerm.fill("white")
        self.alle_celler.draw(self.skjerm)
        pg.draw.rect(self.skjerm, "black", (0, 0, BREDDE, MENY_HØYDE), 2)
        font = pg.font.Font(None, 32)
        tekst = font.render(
            "Trykk S (start), T (tøm) eller N (neste generasjon)", True, "black")
        self.skjerm.blit(tekst, (MARG, MARG-16))
        tekst = font.render(
            "Klikk en celle for å endre tilstand", True, "black")
        self.skjerm.blit(tekst, (MARG, MARG+16))
        pg.display.update()

    def kjør(self):
        """Kjør hovedspilløkken."""
        while self.kjører:
            self.behandle_hendelser()
            self.oppdater()
            self.tegn()
            self.klokke.tick(FPS)
        pg.quit()

    def start(self):
        """Initier rutenettet med tilfeldig levende celler."""
        for celle in self.alle_celler:
            celle.er_død = random() > 1/3

    def tøm(self):
        """Sett alle celler i rutenettet til død tilstand."""
        for celle in self.alle_celler:
            celle.er_død = True

    def neste_generasjon(self):
        """Beregn og sett neste generasjons tilstand for alle celler."""
        for celle in self.alle_celler:
            celle.beregn_neste_tilstand()
        for celle in self.alle_celler:
            celle.er_død = celle.neste_tilstand


if __name__ == "__main__":
    app = App()
    app.kjør()

# Smidig IT-2 © TIP AS 2024
