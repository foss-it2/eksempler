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
        print(self.troll.tags)
    
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

    def handleKeys(self,evt):
        pass
        

class Brikke(Firkant):
    teller = 1
    def __init__(self, w, h, xpos, ypos) -> None:
        super().__init__(w, h, "yellow")
        self.x = xpos
        self.y = ypos
        self.tekst = "M"
        self.tags = self.settId()
    
    def tegnBrikke(self,canvas):
        canvas.create_rectangle(
            self.x - self.w/2,
            self.y - self.h/2,
            self.x + self.w/2,
            self.y + self.h/2,
            fill=self.farge,
            outline="black" # Viktig å ha med outline pga. default er å tegne med lys outline.
        )

    def slettBrikke(self,canvas):
        canvas.delete(self.tags)
    
    def settId(self):
        self.tags = f"id{Brikke.teller}"
        print(self.tags)
        Brikke.teller += 1

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
        self.x += self.vx
        self.y += self.vy
    
    def sjekkKollisjon(self,objekt):
        pass