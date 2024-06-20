# ----------------------------------------------------------------
# REA3049 EKSAMEN V2024 - OPPGAVE 10. Gunnar Stigen, Malakoff vgs.
# Brukergrensesnitt: f: Frys simulering    c: Slett alle celler.
#                    g: Start simulering   klikk: vekker cellen.
# ----------------------------------------------------------------
import time
import random as rd
import pygame as pg
from   pygame.locals import K_c, K_f, K_g  # Clear / Freeze / Go

# Konstanter:
CD = 5  # Cellenes dimensjon (antall piksler hver vei i kvadratet).
CR = 100  # Nettets  dimensjon (antall rader - i høyden
CK = 100  #                      og kolonner - i bredden).
WH = CD * CR  # Vinduets dimensjon (antall piksler i høyden og
WW = CD * CK  #                     antall piksler i bredden).

# Fargetupler:
black = (40, 40, 40)     # Nesten sort (levende celler)
white = (255, 255, 255)  # Hvit (døde celler)

class Cell:   # Lager en felles klasse for alle cellene:
    def __init__(self, r, k, color, size, alive, vindu):
        self.r = r  # rad
        self.k = k  # kolonne
        self.color = color
        self.size = size
        self.alive = alive  # 1 hvis i live, 0 hvis død.
        self.vindu = vindu

    def tegn(self):
        x = CD * round(self.k)
        y = CD * round(self.r)
        pg.draw.rect(self.vindu, self.color, (x, y, self.size, self.size))

    def isAlive(self):
        return self.alive

    def kill(self):
        self.alive = 0
        self.color = white

    def live(self):
        self.alive = 1
        self.color = black

    def nbrs_alive(self):    # Count true neighbour cells that are currently alive.
        nba = 0  # Neighbours alive | List of offsets (as tuples) for 8 neighbours:
        nbo = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        for nbt in nbo:
            nbk = self.k + nbt[0]
            nbr = self.r + nbt[1]
            if nbk >= 0 and nbk < CK and nbr > 0 and nbr < CR:
                nba += cellgrid[nbr][nbk].isAlive()
        return nba

# Tegn alle cellene:
def tegnAlleCeller():
    for r in range(0, CR):
        for k in range(0, CK):
            cell = cellgrid[r][k]
            cell.tegn()
    pg.display.update()

# Oppdater cellenes liv ifølge reglene:
def oppdaterCelleLiv():
    # For ikke å tukle med cellenes tilstand i cellegrid opprettes et
    tempgrid = []  # kladdegrid som definerer neste generasjon celler.
    for r in range(0, CR):
        tempgrid.append([0] * CK)

    # Beregn liv for neste generasjon:
    for r in range(0, CR):
        for k in range(0, CK):
            cell = cellgrid[r][k]
            nba = cell.nbrs_alive()
            if cell.isAlive():
                if nba == 2 or nba == 3:
                    tempgrid[r][k] = 1
            elif nba == 3: # Wake up?
                tempgrid[r][k] = 1

    # Sett ny status i cellene:
    for r in range(0, CR):
        for k in range(0, CK):
            cell = cellgrid[r][k]
            if tempgrid[r][k] == 1:
                cell.live()
            else:
                cell.kill()

# Hovedprogram. Sett opp pygame og et tegnevindu med
pg.init()                # bredde = WW og høyde = WH
vindu = pg.display.set_mode([WW, WH])

# Lag brett med celler:
cellgrid = []
for r in range(0, CR):
    cellgrid.append([0] * CK)

# Lag generasjon 0 med p(alive) = 1/3
for r in range(0, CR):
    for k in range(0, CK):
        if rd.random() < 1/3:
            color = black
            alive = 1
        else:
            color = white
            alive = 0

        cell = Cell(r, k, color, CD, alive, vindu)
        cellgrid[r][k] = cell

# Evig løkke inntil vinduet lukkes:
fortsett = True
simulate = True

while fortsett:
    if simulate:
        tegnAlleCeller()
        time.sleep(0.1)
        oppdaterCelleLiv()

    # Sjekk innkomne hendelser:
    for event in pg.event.get():

        if event.type == pg.KEYDOWN:
            key = event.key
            if key == K_f:     # Frys status?
                simulate = False
            elif key == K_g:   # Fortsett?
                simulate = True
            elif key == K_c:   # Slett alle?
                for r in range(0, CR):
                    for k in range(0, CK):
                        cellgrid[r][k].kill()
                tegnAlleCeller()

        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            rad = pos[1]//CD
            kol = pos[0]//CD
            cellgrid[rad][kol].live()
            tegnAlleCeller()

        elif event.type == pg.QUIT:
            fortsett = False
# Avslutt:
pg.quit()
