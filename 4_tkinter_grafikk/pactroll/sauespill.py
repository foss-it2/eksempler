import pygame as pg
import random as rd

# Importerer piltastene
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Initialiserer/starter pygame
pg.init()

# Fargekart
fargeGrønn = (70, 250, 100)
fargeGul = (255, 255, 0)
fargeGrå = (230, 230, 230)
fargeHvit = (255, 255, 255)
fargeRosa = (255, 150, 255)

# Definerer spillebrettet


class Spillebrett:
    # Vinduet
    høyde = 500
    bredde = 700
    sidefelt = 100  # Bredde på sidefeltene

    vindu = pg.display.set_mode([bredde, høyde])
    font = pg.font.SysFont("Tahoma", 18)

    # Skjermobjektene
    objektSide = 30   # Standard lengde på sidekantene til spillobjektene
    objektListe = []  # Liste for å lagre skjermobjektene

    def leggTilObjekt(self, objekt):
        self.objektListe.append(objekt)

    def fjernObjekt(self, objekt):
        self.objektListe.remove(objekt)


class SpillObjekt:
    """Klasse for å representere et spillobjekt"""

    def __init__(self, x, y, side, farge, bokstav, spillebrett):
        """Konstruktør"""
        self.xPosisjon = x
        self.yPosisjon = y

        # Utseendet til spillobjektene
        self.side = side       # Størrelse på kvadratet
        self.farge = farge
        # M (menneske), M+ (menneske med sau), S (sau), BØ (spøkelse) og H (hinder)
        self.bokstav = bokstav

        self.brett = spillebrett

    # Ikke felles metoder for plassering og flytt siden dette er ulikt for de ulike spillobjekterne
    # Alle spillobjekter tegnes på samme måte
    def tegn(self, vindu, font):
        """Metode for å tegne objektet på skjermen. (x,y) verdier finnes i objektet"""

        # Tegner et kvadrat på (side x side) pixler i posisjonen
        pg.draw.rect(vindu, self.farge, (self.xPosisjon,
                     self.yPosisjon, self.side, self.side))
        firkant = font.render(self.bokstav, True, (0, 0, 0), self.farge)
        vindu.blit(firkant, (self.xPosisjon+2, self.yPosisjon+2))


class Menneske(SpillObjekt):
    """
    Klasse for å lage menneske-objekter. Arver fra klasse SpillObjekt.
    Parametre:
    x (int):        x posisjon
    y (int):        y posisjon
    side (int):     størrelse
    farge (RGB):    farge
    bokstav (str):  M eller M+ hvis bærer sau
    brett (vindow): vinduet
    """

    def __init__(self, x, y, fart, side, farge, bokstav, brett):
        """
        Super klassens konstruktør må også være med
        """
        super().__init__(x, y, side, farge, bokstav, brett)

        self.fart = fart            # Menneskets fart
        self.poeng = 0              # Menneskets poeng
        self.bærerSau = False       # True når sau løftes opp

        self.retning = ""           # høyre/venstre/opp/ned
        self.frysPosisjon = False   # True når objektet treffer hinder eller vegg
        self.gameOver = False       # Er spillet slutt?

    def plassering(self, brett):
        # Plasserer et menneske tilfeldig i sidefeltet til venstre
        x1 = 0
        y1 = 0
        x2 = brett.sidefelt
        y2 = brett.høyde

        # Tuppel med tilfeldig ledig posisjon
        pos = ledigPos(x1, y1, x2, y2, brett.objektListe, brett.objektSide)
        self.xPosisjon = pos[0]
        self.yPosisjon = pos[1]

        self.tegn(brett.vindu, brett.font)
        brett.leggTilObjekt(self)

    def endreRetning(self, retning):  # høyre/venstre/opp/ned
        self.retning = retning

    def flytt(self, brett):
        """Metode for å flytte objektet"""
        if not self.gameOver and not self.frysPosisjon:
            # Flytte mennesket i sin retning med sin fart
            if self.retning == "venstre":
                self.xPosisjon = self.xPosisjon - self.fart
            elif self.retning == "opp":
                self.yPosisjon = self.yPosisjon - self.fart
            elif self.retning == "høyre":
                self.xPosisjon = self.xPosisjon + self.fart
            elif self.retning == "ned":
                self.yPosisjon = self.yPosisjon + self.fart

        # Kollisjon i en av veggene når objektet flyttes. Posisjonen 'fryses'.
        if self.yPosisjon < 0:  # I taket
            self.frysPosisjon = True
        elif self.yPosisjon > brett.høyde - self.side:  # I kjelleren
            self.frysPosisjon = True
        elif self.xPosisjon < 0:    # Venstre
            self.frysPosisjon = True
        elif self.xPosisjon > brett.bredde - self.side:  # Høyre
            self.frysPosisjon = True

        # Sjekke om en sau er levert
        if self.xPosisjon < (brett.sidefelt - self.side):  # Inne i venstre sidefelt
            if self.bærerSau:  # En sau er levert
                self.poeng += 1

                self.bærerSau = False
                self.bokstav = " M"
                self.fart = 0.05  # Normal fart

                # Nytt saueobjekt
                sau = Sau(0, 0, brett.objektSide, fargeRosa, " S", brett.vindu)
                sau.plassering(brett)

                # Nytt hinder
                hinder = Hindring(0, 0, brett.objektSide,
                                  fargeGul, " H", brett.vindu)
                hinder.plassering(brett)

                # Nytt spøkelse
                spøkelse = Spøkelse(0, 0, brett.objektSide,
                                    fargeHvit, "BØ", brett.vindu, 0.02, 0.06)
                spøkelse.plassering(brett)

    def sjekkKollisjon(self, annetObjekt):
        """Sjekker om objektet kolliderer med sau, spøkelse eller hinder"""
        if abs(self.xPosisjon - annetObjekt.xPosisjon) < self.side and abs(self.yPosisjon - annetObjekt.yPosisjon) < self.side:
            return True
        else:
            return False

    def kollisjon(self, annetObjekt, brett):
        # Kollisjon mellom mennesket og et annet objekt
        if annetObjekt.bokstav.strip() == "S":  # Kolliderer med sau
            # Hvis bærer sau så stopper spillet
            if self.bærerSau:
                self.gameOver = True
            else:
                # Fjerne saueobjektet
                brett.fjernObjekt(annetObjekt)

                # Endre bokstav
                self.bokstav = "M+"
                self.bærerSau = True

                # Redusere farten til mennesket
                self.fart = 0.03    # Redusert fart

        elif annetObjekt.bokstav.strip() == "H":
            self.frysPosisjon = True

        elif annetObjekt.bokstav.strip() == "BØ":
            # print("Mennesket kolliderte med et spøkelse.")
            self.gameOver = True


class Spøkelse(SpillObjekt):
    """
    Klasse for å lage spøkelses-objekter. Arver fra klasse SpillObjekt.
    Parametre:
    xPosisjon (int): x posisjon
    yPosisjon (int): y posisjon
    side (int):     størrelse
    farge (RGB):    farge
    bokstav (str):  BØ
    brett (vindow): vinduet
    """

    def __init__(self, x, y, side, farge, bokstav, brett, xFart, yFart):
        """
        Super klassens konstruktør må også være med
        """
        super().__init__(x, y, side, farge, bokstav, brett)

        self.xFart = xFart
        self.yFart = yFart

    def plassering(self, brett):
        # Plasserer dette spøkelset tilfeldig i hovedvinduet
        # Øvre venstre hjørne
        x1 = brett.sidefelt
        y1 = 0
        # Nedre venstre hjørne
        x2 = brett.bredde - brett.sidefelt
        y2 = brett.høyde

        # Tuppel med tilfeldig ledig posisjon
        pos = ledigPos(x1, y1, x2, y2, brett.objektListe, brett.objektSide)

        self.xPosisjon = pos[0]
        self.yPosisjon = pos[1]

        brett.leggTilObjekt(self)
        self.tegn(brett.vindu, brett.font)

    def flytt(self, brett):
        # Sjekker om spøkelset er utenfor høyre/venstre kant av hovedvindu
        if (self.xPosisjon <= brett.sidefelt or (self.xPosisjon + self.side) >= (brett.bredde - brett.sidefelt)):
          self.xFart = -self.xFart

        # Sjekker om spøkelset er utenfor øvre/nedre kant
        if (self.yPosisjon <= 0 or (self.yPosisjon + self.side) >= brett.høyde):
          self.yFart = -self.yFart

        # Flytter spøkelset
        self.xPosisjon += self.xFart
        self.yPosisjon += self.yFart


class Hindring(SpillObjekt):
    """
    Klasse for å lage hinder-objekter. Arver fra klasse SpillObjekt.
    Parametre:
    xPosisjon (int):    x posisjon
    yPosisjon (int):    y posisjon
    side (int):         størrelse kvadrat
    farge (RGB):        farge
    bokstav (str):      H
    brett (vindow):     vinduet
    """

    def __init__(self, x, y, side, farge, bokstav, brett):
        """
        Super klassens konstruktør må også være med
        """
        super().__init__(x, y, side, farge, bokstav, brett)

    def plassering(self, brett):
        # Plasserer dette hinderobjektet tilfeldig i hovedvinduet
        x1 = brett.sidefelt
        y1 = 0
        x2 = brett.bredde - brett.sidefelt
        y2 = brett.høyde
        # Tuppel med tilfeldig ledig posisjon
        pos = ledigPos(x1, y1, x2, y2, brett.objektListe, brett.objektSide)

        self.xPosisjon = pos[0]
        self.yPosisjon = pos[1]

        self.tegn(brett.vindu, brett.font)
        brett.leggTilObjekt(self)


class Sau(SpillObjekt):
    """
    Klasse for å lage saue-objekter. Arver fra klasse SpillObjekt.
    Parametre:
    xPosisjon (int):    x posisjon
    yPosisjon (int):    y posisjon
    side (int):         størrelse kvadrat
    farge (RGB):        farge
    bokstav (str):      S
    brett (vindow):     vinduet
    """

    def __init__(self, x, y, side, farge, bokstav, brett):
        """
        Super klassens konstruktør må også være med
        """
        super().__init__(x, y, side, farge, bokstav, brett)

    def plassering(self, brett):
        # Plasserer en sau tilfeldig i sidefeltet til høyre
        x1 = brett.bredde - brett.sidefelt
        y1 = 0
        x2 = brett.bredde
        y2 = brett.høyde

        # Tuppel med tilfeldig ledig posisjon
        pos = ledigPos(x1, y1, x2, y2, brett.objektListe, brett.objektSide)
        self.xPosisjon = pos[0]
        self.yPosisjon = pos[1]

        self.tegn(brett.vindu, brett.font)
        brett.leggTilObjekt(self)


def ledigPos(x1, y1, x2, y2, objekter, kvadrat):
    ''' Funksjon for å finne ledig posisjon innenfor en del av vinduet.
        (x1,y1) (int,int): øvre venstre hjørne
        (x2,y2) (int,int): nedre høyre hjørne
        objekter (liste) : objekter som kan sperre for plassering
        kvadrat  (int)   : størrelse på side i kvadrat som skal plasseres
    Returnerer en posisjon (x,y) som har plass til kvadratet.'''

    x = rd.randint(x1, x2 - kvadrat)
    y = rd.randint(y1, y2 - kvadrat)

    opptatt = True
    while opptatt:
        # Finne en posisjon som ingen av skjermobjektene sperrer for.
        opptatt = False  # Settes til True hvis et objekt sperrer

        for o in objekter:
            if (abs(x - o.xPosisjon) < kvadrat and abs(y - o.yPosisjon) < kvadrat):
                opptatt = True  # Posisjonen er opptatt
        if opptatt:
            # Trekke på nytt til finner ledig pos
            x = rd.randint(x1, x2 - kvadrat)
            y = rd.randint(y1, y2 - kvadrat)
        else:
            return x, y


brett = Spillebrett()

# Plassere et menneske objekt tilfeldig i frisonen til venstre
menneske = Menneske(0, 0, 0.05, brett.objektSide,
                    fargeGrønn, " M", brett.vindu)
menneske.plassering(brett)

# Lage et spøkelsesobjekt i hovedvinduet
spøkelse = Spøkelse(0, 0, brett.objektSide, fargeHvit,
                    "BØ", brett.vindu, 0.02, 0.05)
spøkelse.plassering(brett)

# Plassere tre hinderobjekter tilfeldig i hovedvinduet
for i in range(3):
    hinder = Hindring(0, 0, brett.objektSide, fargeGul, " H", brett.vindu)
    hinder.plassering(brett)

# Plassere tre saueobjekter tilfeldig i frisonen til høyre
for i in range(3):
    sau = Sau(0, 0, brett.objektSide, fargeRosa, " S", brett.vindu)
    sau.plassering(brett)

fortsett = True
# Gjenta helt til vinduet lukkes
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    taster = pg.key.get_pressed()

    # Endrer retning hvis en piltast er trykket
    if taster[K_UP]:
        menneske.endreRetning("opp")
        menneske.frysPosisjon = False
    elif taster[K_DOWN]:
        menneske.endreRetning("ned")
        menneske.frysPosisjon = False
    elif taster[K_LEFT]:
        menneske.endreRetning("venstre")
        menneske.frysPosisjon = False
    elif taster[K_RIGHT]:
        menneske.endreRetning("høyre")
        menneske.frysPosisjon = False

    # Farger bakgrunnen sort
    brett.vindu.fill((0, 0, 0))

    # Tegner sidefeltene
    pg.draw.rect(brett.vindu, fargeGrå, (0, 0, 100, 500))
    pg.draw.rect(brett.vindu, fargeGrå, (600, 0, 100, 500))

    # Vise alle spillobjekter
    for o in brett.objektListe:
        o.tegn(brett.vindu, brett.font)

    # Melding på skjermen
    melding = "  Poeng: " + str(menneske.poeng)

    if not menneske.gameOver:
        menneske.flytt(brett)  # Flytte mennesket

        # Flytte spøkelser
        for o in brett.objektListe:
            if o.bokstav.strip() == "BØ":
                o.flytt(brett)

        # Sjekke om mennesket kolliderer med ett av de andre objektene
        for o in brett.objektListe:
            if menneske.sjekkKollisjon(o):
                menneske.kollisjon(o, brett)
    else:
        melding += ". Game over.  "

    # Vise melding på skjermen
    bilde = brett.font.render(melding, True, (0, 0, 0), (255, 150, 150))
    brett.vindu.blit(bilde, (5, 5))

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
