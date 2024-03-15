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


""" 
Objekt
    Inneholder alt om kollisjoner med andre objekter.
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

"""


class Spill:
    def __init__(self, objekter=[]) -> None:
        self.objekter = objekter
        self.heks = None
        self.player = None
    
    def tegn(self):
        """ Tegner alle objekter i listen"""
        for obj in self.objekter:
            obj.tegn()
        self.heks.tegn()
        self.player.tegn()
    
    def fjernOgOppdater(self):
        """# Fjern alle objekter i listen og oppdater"""
        for obj in self.objekter:
            obj.fjern()
            obj.oppdater()  # Oppdaterer posisjon og eventuelt fart.
        self.player.fjern()
        self.player.oppdater()
        self.heks.fjern()
        self.heks.oppdater(self.objekter)
    
    def kollisjon(self):
        """Sjekker kollisjon med vegger og med andre objekter."""
        for obj in self.objekter:
            obj.sjekkKollisjonVegger()
        self.player.sjekkKollisjonVegger()
        # Sjekker kollisjon mellom objekt og heksa ved å sende ved en liste med objekter som kollisjon skal sjekkes for.
        for obj in self.objekter:
            self.heks.sjekkKollisjon(self,obj) # Sender med selve spillet som parameter også.
            self.player.sjekkKollisjon(self,obj)
    
    def slett(self,objekt):
        self.objekter.remove(objekt)
    
    def leggTilNPC(self):
        xpos = randint(20, canvas_width-20)
        ypos = randint(20, canvas_height-20)
        # Passer på at posisjonene ikke finnes fra før, og at de ikke er lik heksa.
        posisjoner = []
        for obj in self.objekter:
            posisjoner.append([obj.x,obj.y])
        while [xpos,ypos] in posisjoner and (self.heks.x != xpos and self.heks.y != ypos):
            xpos = randint(20, canvas_width-20)
            ypos = randint(20, canvas_height-20)
        self.objekter.append(NPC(xpos,ypos))


class Objekt:
    """
        Firkantet objekt som er superklasse.
        Inneholder basismetodene som tegning, fjerning, kollisjonshåndtering.
        Kollisjon må håndteres ved å se på overlapp av to rektangler. Ikke Pythagoras som for sirkel.
    """
    def __init__(self, navn,
                 xpos=canvas_width/2,
                 ypos=canvas_height/2,
                 x_fart=0, y_fart=0,
                 fill="#ffff00", outline="#ffff00",
                 lengde = 20, bredde = 15):
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
        canvas.create_rectangle(self.x-self.l, self.y-self.b,
                           self.x+self.l, self.y+self.b,
                           fill=self.fill, outline=self.outline, tags=self.tag)

    def fjern(self):
        canvas.delete(self.tag)

    def oppdater(self):
        self.x += self.x_fart
        self.y += self.y_fart

class Player(Objekt):
    def __init__(self):
        self.x_retning = 1
        self.y_retning = 0
        super().__init__("Player", 40,canvas_height-40, 2, 2, "dodgerblue", "dodgerblue", 20, 20)
    
    def oppdater(self):
        self.x += self.x_fart * self.x_retning
        self.y += self.y_fart * self.y_retning
    
    def sjekkKollisjon(self, spill, objekt):
        global isRunning
        # Sjekk kollisjon mellom Player og objektet:
        # Beregner overlapp av rektangler for å finne kollisjon
        if abs(self.x - objekt.x) <= self.l + objekt.l and abs(self.y - objekt.y) <= self.b + objekt.b and not objekt.aktiv:
            # Befri steinen
            print("Traff stein")
            spill.objekter.remove(objekt)


class Heks(Objekt):
    def __init__(self,):
        self.target = None
        super().__init__("heks", canvas_width/4, canvas_height /
                         4, 0, 0, "OrangeRed", "OrangeRed", 20, 20)
    
    def oppdater(self, objekter):
        """Utvider super-metoden"""
        super().oppdater()
        self.pickTarget(objekter)
    
    def sjekkKollisjon(self, spill, objekt):
        global isRunning
        # Sjekk kollisjon mellom heks og objektet:
        # Beregner overlapp av rektangler for å finne kollisjon
        if abs(self.x - objekt.x) <= self.l + objekt.l and abs(self.y - objekt.y) <= self.b + objekt.b and objekt.aktiv:
            # Flytt heksa ett hakk tilbake
            self.x -= self.x_fart
            self.y -= self.y_fart
            #isRunning = False
            objekt.stein()
            spill.leggTilNPC()

    
    def pickTarget(self, objekter):
        d_min = 1e30
        self.target = objekter[0]
        for objekt in objekter:
            if not objekt.aktiv:
                continue
            if objekt.tag == self.tag:  # Hvis objektet som sjekkes er seg selv.
                continue
            # Beregner avstand og oppdaterer
            dx = abs(objekt.x-self.x)
            dy = abs(objekt.y-self.y)
            d = (dx**2 + dy**2)**0.5
            if d < d_min:
                d_min = d
                self.target = objekt # Setter objektet som target for heksa.
        # Etter for-loop har heksa bestemt seg for target.
        # Bergner retning for heksa.
        print(f"Target er nå: {self.target.tag}")
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        # Beregner fart. Setter den lengste aksen som høyeste fart, den andre aksen som en brøkdel av dette.
        if abs(dx) > abs(dy):
            xfaktor = 1
            try:
                yfaktor = abs(dy)/abs(dx)
            except:
                yfaktor = 1
        else:
            yfaktor = 1
            try:
                xfaktor = abs(dx)/abs(dy)
            except:
                xfaktor = 1
        # Setter fartene.
        if dx > 0:
            self.x_fart = xfaktor
        else:
            self.x_fart = -xfaktor
        if dy > 0:
            self.y_fart = yfaktor
        else:
            self.y_fart = -yfaktor


            

class NPC(Objekt):
    teller = 1
    def __init__(self,xpos = canvas_width/2, ypos = canvas_height/2):
        self.aktiv = True        
        super().__init__(f"NPC{NPC.teller}", xpos, ypos, 0, 0, "#ffff00", "#ffff00", 20, 20)
        NPC.teller += 1 # Øker klassevariabelen med 1.
    
    def stein(self):
        self.aktiv = False
        self.fill = "#d3d3d3"

    def befri(self):
        slettObjekt(self) # sletter seg selv ved å kalle opp global funksjon.

def slettObjekt(objekt):
    spill.slett(objekt) 

#firkantA = Objekt("FirkantA", canvas_width/3-20, 20, 0, 3, "yellow", "yellow")
#firkantB = Objekt("FirkantB", canvas_width/2, 3*canvas_height/4, 0, -3, "deeppink", "white")


spill = Spill()
spill.leggTilNPC()
spill.leggTilNPC()

spill.heks = Heks()

spill.player = Player()



# avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()


def handle_avslutt(event):
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

avslutt.bind("<Button-1>", handle_avslutt)

# Tastetrykk
window.bind("<Key>",processKeypress)


# Her animinerer vi
teller = 0
isRunning = True
while isRunning == True:
    # Tegn alle objekter i listen
    spill.tegn()
    canvas.after(1)  # venter 100 ms
    canvas.update()
    # Fjern alle sirkler i listen og oppdater posisjoner og fart for objeker
    spill.fjernOgOppdater()
    # Sjekker kollisjon med vegger og med andre objekter.
    spill.kollisjon()
    teller += 1

spill.tegn()


window.mainloop()
