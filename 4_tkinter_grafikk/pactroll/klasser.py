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
    
    def oppdater(self):
        # Slett alle ting i canvas
        for brikke in self.brikker:
            brikke.slettBrikke(self.canvas)
        # Utføre flytting

        # Sjekk kollisjon

        # Tegne på nytt
        for brikke in self.brikker:
            print(brikke.tags)
            brikke.tegnBrikke(self.canvas)

    def leggUtMat(self):
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
            fill=self.farge
        )

    def slettBrikke(self,canvas):
        canvas.delete(self.tags)
    
    def settId(self):
        self.tags = f"id{Brikke.teller}"
        Brikke.teller += 1
