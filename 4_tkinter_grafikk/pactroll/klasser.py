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
        # Slett alle ting i canvas
        for brikke in self.brikker:
            brikke.slettBrikke(self.canvas)
        self.troll.slettBrikke(self.canvas)
        
        # Utføre flytting
        self.troll.endrePos()

        # Sjekk kollisjon

        # Tegne på nytt
        for brikke in self.brikker:
            brikke.tegnBrikke(self.canvas)
        self.troll.tegnBrikke(self.canvas)

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
    
    def sjekkKollisjon(self,objekt):
        pass