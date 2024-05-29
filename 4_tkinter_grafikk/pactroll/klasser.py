"""
Klasser for Pactroll
"""

class Firkant:
    def __init__(self, w, h, farge) -> None:
        self.w = w
        self.h = h
        self.farge = farge

class Spill(Firkant):
    def __init__(self, w, h,brikker=[],canvas=None) -> None:
        super().__init__(w, h, "black")
        self.brikker = brikker
        self.canvas = canvas
        self.troll = Troll(30,200)
    
    def oppdater(self):        
        # Utføre flytting
        self.troll.endrePos()

        # Sjekk kollisjon
        fortsett = self.troll.sjekkKollisjon(self.w, self.h, self.brikker)  # Returnerer False hvis den kolliderer med vegg eller hindring.
        if fortsett == False:
            # Hvis troll kolliderer med noe den ikke skal stanses spillet.
            return False

        # Slett alle ting i canvas
        for brikke in self.brikker:
            brikke.slettBrikke(self.canvas)
        self.troll.slettBrikke(self.canvas)

        # Tegne på nytt
        for brikke in self.brikker:
            brikke.tegnBrikke(self.canvas)
        self.troll.tegnBrikke(self.canvas)

        return True

    def leggUtMat(self):
        # 1) Tilfeldig funksjon
        pass

    def handleKeys(self,key):
        if key == "Up":
            self.troll.endreRetning("y",-1)
        elif key == "Right":
            self.troll.endreRetning("x",1)
        elif key == "Down":
            self.troll.endreRetning("y",1)
        elif key == "Left":
            self.troll.endreRetning("x",-1)
        

class Brikke(Firkant):
    teller = 0
    def __init__(self, w, h, xpos, ypos) -> None:
        super().__init__(w, h, "yellow")
        self.x = xpos
        self.y = ypos
        self.tekst = "M"
        self.tags = self.settId()
    
    def tegnBrikke(self,cnv):
        cnv.create_rectangle(
            self.x - self.w/2,
            self.y - self.h/2,
            self.x + self.w/2,
            self.y + self.h/2,
            fill=self.farge,
            outline=self.farge, # Viktig å ha med outline pga. default er å tegne med lys outline.
            tags = self.tags
        )

    def slettBrikke(self,cnv):
        cnv.delete(self.tags)
    
    def settId(self):
        Brikke.teller += 1
        return f"id{Brikke.teller}"
    
    def __str__(self):
        return f"{self.tags}: x{self.x},y{self.y}"


class Troll(Brikke):
    def __init__(self, xpos, ypos) -> None:
        super().__init__(30, 30, xpos, ypos)
        self.vx = 1
        self.vy = 0
        self.poeng = 0
        self.farge = "chartreuse"
        
    def endreRetning(self,retning, verdi):
        if retning == "x":
            self.vx = verdi # +-1
            self.vy = 0
        else:
            self.vx = 0
            self.vy = verdi
    
    def endrePos(self):
        self.x += self.vx * 5
        self.y += self.vy * 5
    
    def sjekkKollisjon(self, w, h, brikker):
        # Returnerer False hvis kollisjon med vegg eller hindring, ellers True.
        # Sjekker kollisjon med vegger
        veggkollisjon = self.sjekkKollisjonVegg(w, h)
        if veggkollisjon == True:
            return False
        # Sjekke kollisjon med hindring
        
        # Sjekker kollisjon med mat
        # Lager en liste med mat som trollet går gjennom. Alle nye kollisjoner sjekkes for om de allerede ligger i denne listen.
        matkollisjon_liste = []
        nye_mat_kollisjoner,hindring = self.sjekkKollisjonBrikker(brikker)
        if len(hindring) > 0:
            print("kollisjon hindring")
            return False
        # Går gjennom matkollisjon_listen og sjekker om noen ikke er underveis i kollisjon
        for brikke in matkollisjon_liste:
            print(brikke)
            if brikke not in nye_mat_kollisjoner:
                # Gjør om til hindring
                print("gjør om til hindring")
                brikke.tekst = "H"
                brikke.farge = "grey"
                matkollisjon_liste.remove(brikke)
        # Legg til nye brikker i matkollisjon_liste
        matkollisjon_liste = matkollisjon_liste + nye_mat_kollisjoner
        # Dersom ikke noe annet gjør at vi skal stoppe spillet
        return True
    
    def sjekkKollisjonVegg(self,w, h):
        if self.x + self.w/2 > w:
            # Setter ny posisjon rett inntil vegg
            self.x = w - self.w/h
            print("kollisjon ")
            return True
        elif self.x - self.w/2 < 0:
            self.x = self.w/2
            return True
        elif self.y - self.h/2 < 0:
            self.y = self.h/2
            return True
        elif self.y + self.h/2 > h:
            self.y = h - self.h/2
            return True
        return False
    
    def sjekkKollisjonBrikker(self, brikker):
        # Sjekk overlapp mellom brikke og objekt
        # Lager en liste med overlapp med mat og hindring.
        mat = []
        hindring = []
        for brikke in brikker:
            if self.overlapper(brikke):
                if brikke.tekst == "M":
                    mat.append(brikke)
                else:
                    hindring.append(brikke)
        return mat,hindring

    def overlapper(self, other):
        # Sjekker for om det IKKE er overlapp.
        # Returnerer motsatt boolean verdi.
        if (self.x + self.w / 2 <= other.x - other.w / 2 or  # this right edge is left of other's left edge
            self.x - self.w / 2 >= other.x + other.w / 2 or  # this left edge is right of other's right edge
            self.y + self.h / 2 <= other.y - other.h / 2 or  # this bottom edge is above other's top edge
            self.y - self.h / 2 >= other.y + other.h / 2):  # this top edge is below other's bottom edge
            return False
        return True
        
