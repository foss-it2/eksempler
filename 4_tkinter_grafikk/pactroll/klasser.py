"""
Klasser for Pactroll
"""

class Firkant:
    def __init__(self, w, h) -> None:
        self.w = w
        self.h = h

class Spill(Firkant):
    def __init__(self, w, h,brikker=[],canvas) -> None:
        super().__init__(w, h)
        self.brikker = brikker
        self.canvas = canvas
    
    def oppdater(self):
        pass

    def leggUtMat(self):
        pass

    def handleKeys(self,evt):
        pass

class Brikke(Firkant):
    def __init__(self, w, h, xpos, ypos) -> None:
        super().__init__(w, h)
        self.x = xpos
        self.y = ypos
        self.tekst = "M"
    
    def tegnBrikke(self,canvas):
        pass

    def slettBrikke(self,canvas):
        pass
