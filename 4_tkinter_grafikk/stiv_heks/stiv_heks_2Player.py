import tkinter as tk
from random import randint

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 800
canvas_height = 500
canvas_width = windowWidth
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.

# 1) Lager en header for overskrift
header = tk.Canvas(frame1, width=windowWidth, height=100)
header.pack()
overskrift = tk.Label(header, text="Stiv heks.")
overskrift.pack()

# 2) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=canvas_width,
                   height=canvas_height, background="black")
canvas.pack()

poeng1 = tk.Label(text=f"Player 1: 0 poeng")
poeng1.pack()
poeng2 = tk.Label(text=f"Player 2: 0 poeng")
poeng2.pack()


""" 
Beskrivelser av klasser
Objekt
    Superklasse som inneholder basismetoder.
De tre underklassene arver fra Objekt:
Heks
    Automatisk targeting av NPC eller Player.
    Target av den som er nærmest, men ikke grå inaktive NPC.
    Teleporterer gjennom vegger.
    Heks øker farten for hver 3. NPC som befris.
NPC
    Tilfeldig posisjon.
    Står stille.
    Endrer farge ved kollisjon med Heks fra grønn til grå.
    NPC forsvinner når den er befridd etter en viss tid.
    NPC forblir på brettet ved befrielse så heks kan ta den en gang til.
Player
    Beveger seg automatisk i én akse x, eller y.
    Piltaster endrer retning slik som for pacman.
    Kan befri en NPC
    Poeng øker når man befrir en NPC.
    Spillet er slutt når man har oppnådd 10 poeng.

    Oppgaver som skal gjøres.
    1. Legge ut NPC tilfeldig
    2. Påse  at man ikke legger NPC oppå en eksisterende. (Sjekk for x-pos og y-pos intervaller)
    4. Animere Player
    5. Kollisjon mellom NPC og Player. 
    6. Når man kolliderer skal NPC forsvinne.
    7. Poeng for hver NPC man kolliderer med.
    8. Heks-klassen
    9. Tilfeldig bevegelse av heksa
    10. Heks pickTarget for å bestemme bevegelsen.
    11. Teleportere gjennom vegger.
    12. Bokstav inni objekter.

"""


class Spill:
    def __init__(self, objekter=[]) -> None:
        self.objekter = objekter
        self.heks = None
        self.player = None
        self.isRunning = True
        self.player2 = None
    
    def tegn(self):
        """ Tegner alle objekter i listen"""
        for obj in spill.objekter:
            obj.tegn()
        self.player.tegn()
        self.player2.tegn()
    
    def fjernOgOppdater(self):
        """# Fjern alle objekter i listen samt player, og oppdater"""
        for obj in spill.objekter:
            obj.fjern()
            obj.oppdater()
        self.player.fjern()
        self.player2.fjern()
        self.player.oppdater()
        self.player2.oppdater()
    
    def kollisjon(self):
        """Sjekker kollisjon med vegger og med andre objekter."""
        self.player.sjekkKollisjonVegger()
        self.player2.sjekkKollisjonVegger()
        for obj in self.objekter:
            self.player.sjekkKollisjon(self, obj)
            self.player2.sjekkKollisjon(self, obj)
    
    def slett(self,objekt):
        """Sletter et objekt totalt fra spillet."""
        self.objekter.remove(objekt)
    
    def leggTilNPC(self):
        """1) Tilfeldig posisjon for en NPC
            2) Legg NPC inni listen i spill-objektet
        """
        x = randint(25, canvas_width-25)
        y = randint(25, canvas_height-25)
        # Sjekker koordinatene til alle objekter.
        while not self.sjekkGyldigKoordinat(x, y):
            x = randint(25, canvas_width-25)
            y = randint(25, canvas_height-25)
        self.objekter.append(NPC(x, y))  # Legger nytt objekt inn i listen.

    def sjekkGyldigKoordinat(self, x, y):
        for objekt in self.objekter:
            if abs(x - objekt.x) <= 25 + objekt.l and abs(y - objekt.y) <= 25 + objekt.b:
                return False
        return True

    def oppdaterPoeng(self):
        # Oppdaterer begge tekstboksene
        poeng1["text"] = f"Player 1: {spill.player.poeng} poeng"
        poeng2["text"] = f"Player 2: {spill.player2.poeng} poeng"

class Objekt:
    """
        Firkantet objekt som er superklasse.
        Inneholder basismetodene som tegning, fjerning, kollisjonshåndtering.
    """
    def __init__(self, navn,
                 xpos=canvas_width/2,
                 ypos=canvas_height/2,
                 x_fart=0, y_fart=0,
                 fill="#ffff00", outline="#ffff00",
                 lengde = 20, bredde = 20):
        self.l = lengde
        self.b = bredde  # bredde
        self.x = xpos
        self.y = ypos  # Plasserer i midten av vinduet
        self.fill = fill
        self.outline = outline
        self.x_fart = x_fart
        self.y_fart = y_fart
        self.x_retning = 1
        self.y_retning = 0
        self.tag = navn

    def __str__(self):
        return f"{self.tag}"

    def sjekkKollisjonVegger(self):
        """Sjekker kollisjon med alle vegger"""
        global isRunning
        # bunnen
        if self.y + self.b >= canvas_height:
            self.y_retning = -1
            # Flytter seg selv HELT vekk fra vegg i tilfelle den setter seg fast.
            self.y = canvas_height - self.b
        # venstre
        if self.x - self.l <= 0:
            self.x_retning = 1
            self.x = self.l
        # topp
        if self.y - self.b <= 0:
            self.y_retning = 1
            self.y = self.b
        # høyre
        if self.x + self.l >= canvas_width:
            self.x_retning = -1
            self.x = canvas_width - self.l
            

    def tegn(self):
        """Ber canvas om å tegne objektet."""
        canvas.create_rectangle(self.x-self.l, self.y-self.b,
                           self.x+self.l, self.y+self.b,
                           fill=self.fill, outline=self.outline, tags=self.tag)

    def fjern(self):
        """Sletter objekt fra tegningen."""
        canvas.delete(self.tag)

    def oppdater(self):
        """Oppdaterer farten"""
        self.x += self.x_fart
        self.y += self.y_fart

class Player(Objekt):
    """Bevegelig helt!"""
    def __init__(self,farge="dodgerblue", navn="Player"):
        self.x_retning = 1
        self.y_retning = 0
        self.poeng = 0
        super().__init__(navn, 40,canvas_height-40, 3, 3, farge, farge, 20, 20)
    
    def oppdater(self):
        """Må oppdatere posisisjon og fart"""
        self.x += self.x_fart * self.x_retning
        self.y += self.y_fart * self.y_retning
    
    def sjekkKollisjon(self, spill, objekt):
        """Kollisjon må håndteres ved å se på overlapp av to rektangler. Ikke Pythagoras som for sirkel."""
        if abs(self.x - objekt.x) <= self.l + objekt.l and abs(self.y - objekt.y) <= self.b + objekt.b:
            print("kollisjon")
            #spill.isRunning = False
            # sletter NPC-objekter
            spill.slett(objekt)
            antall = randint(1,3)
            for i in range(antall):
                if len(spill.objekter) <= 5:
                    spill.leggTilNPC()
            self.poeng += 1
            if self.poeng >= 50:
                spill.isRunning = False
            spill.oppdaterPoeng()


            

class NPC(Objekt):
    """Stillestående objekt som skal tas av heks, men befris av Player."""
    teller = 1
    def __init__(self,xpos = canvas_width/2, ypos = canvas_height/2):
        self.aktiv = True        
        super().__init__(f"NPC{NPC.teller}", xpos, ypos, 0, 0, "#ffff00", "#ffff00", 20, 20)
        NPC.teller += 1 # Øker klassevariabelen med 1.
    
    def stein(self):
        """Gjør om NPC til en stein hvis den tas av heksa."""
        pass

    def befri(self):
        """Fjerner NPC fra spillet"""
        pass



spill = Spill()
"""1) Legg til en eller flere NPC"""
spill.leggTilNPC()


""" Lag player"""
spill.player = Player(navn="Player1")
spill.player2 = Player("peachpuff", navn="Player2")
spill.player2.x_retning = 0
spill.player2.y_retning = -1


"""Lag en heks"""



# avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()

def handle_avslutt(event):
    spill.isRunning = False
    window.destroy()


def processKeypress(evt):
    key = evt.keysym
    print(f'key: {key}')
    if key == "Left":
        spill.player.x_retning = -1
        spill.player.y_retning = 0
    elif key == "Up":
        spill.player.x_retning = 0
        spill.player.y_retning = -1
    elif key == "Right":
        spill.player.x_retning = 1
        spill.player.y_retning = 0
    elif key == "Down":
        spill.player.x_retning = 0
        spill.player.y_retning = 1
    if key == "a":
        spill.player2.x_retning = -1
        spill.player2.y_retning = 0
    elif key == "w":
        spill.player2.x_retning = 0
        spill.player2.y_retning = -1
    elif key == "d":
        spill.player2.x_retning = 1
        spill.player2.y_retning = 0
    elif key == "s":
        spill.player2.x_retning = 0
        spill.player2.y_retning = 1

avslutt.bind("<Button-1>", handle_avslutt)

# Tastetrykk
window.bind("<Key>",processKeypress)


# Her animinerer vi
while spill.isRunning == True:
    # Tegn alle objekter i listen
    spill.tegn()
    canvas.after(10)  # venter 100 ms
    canvas.update()
    # Fjern alle objekter i canvas, oppdater posisjoner og fart for alle.
    spill.fjernOgOppdater()
    # Sjekker kollisjon med vegger og med andre objekter.
    spill.kollisjon()

spill.tegn() # tegner alle objekter til slutt en siste gang
if spill.player.poeng > spill.player2.poeng:
    print("Player 1 vant!")
else:
    print("Player 2 vant!")



window.mainloop()
