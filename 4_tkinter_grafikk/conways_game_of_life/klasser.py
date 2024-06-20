"""
Klasser for simuleringen Conways game of life
"""

from random import choice

class Celle:
    def __init__(self,i,j,x,y,width=5,outline="black",fill="black") -> None:
        self.w = width
        self.levende = self.setLevende()
        self.nesteTilstand = self.levende
        self.outline = outline
        self.fill = fill
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.id = f"{i},{j}"
        self.rect = None
    
    def tegn(self,cnv):
        self.levende = self.nesteTilstand
        if self.levende == False:
            self.fill = "white"
        else:
            self.fill = "black"
        self.rect = cnv.create_rectangle(
            self.x - self.w/2,
            self.y - self.w/2,
            self.x + self.w/2,
            self.y + self.w/2,
            fill=self.fill,
            outline=self.outline,
            width=1,
            tags = self.id
        )
    
    def oppdaterFarge(self,cnv):
        self.levende = self.nesteTilstand
        if self.levende == False:
            self.fill = "white"
        else:
            self.fill = "black"
        cnv.itemconfig(self.rect, fill=self.fill)
    
    def setLevende(self):
        return choice([True, False, False])  # 1/3 sjanse for å være levende.

    def isPressed(self, x, y):
        # Trekker fra bredden til outline så man ikke kan klikke mellom to celler.
        if self.x+1-self.w/2 <= x <= self.x-1 + self.w/2 and \
            self.y+1-self.w/2 <= y <= self.y-1+self.w/2:
            # Flipper tilstanden levende/død
            self.levende = not self.levende
            self.nesteTilstand = not self.nesteTilstand
            return self.id
        else:
            return False
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i-1][j-1].levende, cells[i-1][j].levende, cells[i-1][j+1].levende, \
            cells[i][j+1].levende, cells[i+1][j+1].levende, cells[i+1][j].levende, \
            cells[i+1][j-1].levende, cells[i][j-1].levende

class TL(Celle):
    """Top Left"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j+1].levende, cells[i+1][j+1].levende, cells[i+1][j].levende

class TR(Celle):
    """Top Right"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j-1].levende, cells[i+1][j-1].levende, cells[i+1][j].levende

class BL(Celle):
    """Bottom Left"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j+1].levende, cells[i-1][j+1].levende, cells[i-1][j].levende

class BR(Celle):
    """Bottom Right"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j-1].levende, cells[i-1][j-1].levende, cells[i-1][j].levende

class TopRow(Celle):
    """Top Row"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j-1].levende, cells[i+1][j-1].levende, cells[i+1][j].levende, \
            cells[i+1][j+1].levende, cells[i][j+1].levende

class BottomRow(Celle):
    """Bottom Row"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j-1].levende, cells[i-1][j-1].levende, cells[i-1][j].levende, \
            cells[i-1][j+1].levende, cells[i][j+1].levende

class LeftEdge(Celle):
    """Left Edge"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i-1][j].levende, cells[i-1][j+1].levende, cells[i][j+1].levende, \
            cells[i+1][j+1].levende, cells[i+1][j].levende

class RightEdge(Celle):
    """Right Edge"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i-1][j].levende, cells[i-1][j-1].levende, cells[i][j-1].levende, \
            cells[i+1][j-1].levende, cells[i+1][j].levende

