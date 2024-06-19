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
    
    def tegn(self,cnv):
        self.levende = self.nesteTilstand
        if self.levende == False:
            self.fill = "white"
        else:
            self.fill = "black"
        cnv.create_rectangle(
            self.x - self.w/2,
            self.y - self.w/2,
            self.x + self.w/2,
            self.y + self.w/2,
            fill=self.fill,
            outline=self.outline,
            width=2,
            tags = self.id
        )
    
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
        return cells[i-1][j-1], cells[i-1][j], cells[i-1][j+1], \
            cells[i][j+1], cells[i+1][j+1], cells[i+1][j], \
            cells[i+1][j-1], cells[i][j-1]

class TL(Celle):
    """Top Left"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j+1], cells[i+1][j+1], cells[i+1][j]

class TR(Celle):
    """Top Right"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j-1], cells[i+1][j-1], cells[i+1][j]

class BL(Celle):
    """Bottom Left"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j+1], cells[i-1][j+1], cells[i-1][j]

class BR(Celle):
    """Bottom Right"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j-1], cells[i-1][j-1], cells[i-1][j]

class TopRow(Celle):
    """Top Row"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j-1], cells[i+1][j-1], cells[i+1][j], \
            cells[i+1][j+1], cells[i][j+1]

class BottomRow(Celle):
    """Bottom Row"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i][j-1], cells[i-1][j-1], cells[i-1][j], \
            cells[i-1][j+1], cells[i][j+1]

class LeftEdge(Celle):
    """Left Edge"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i-1][j], cells[i-1][j+1], cells[i][j+1], \
            cells[i+1][j+1], cells[i+1][j]

class RightEdge(Celle):
    """Right Edge"""
    def __init__(self, id, x, y, width=5, outline="black", fill="black") -> None:
        super().__init__(id, x, y, width, outline, fill)
    
    def getNaboer(self,cells):
        i = self.i
        j = self.j
        return cells[i-1][j], cells[i-1][j-1], cells[i][j-1], \
            cells[i+1][j-1], cells[i+1][j]


class Conways:
    def __init__(self,cells,hoyde,bredde) -> None:
        self.fun = True
        self.cells = cells
        self.hoyde = hoyde
        self.bredde = bredde
    
    def oppdater(self):
        for i in range(self.hoyde):
            for j in range(self.bredde):
                celle = self.cells[i][j]
                # Sjekk naboer
                levende = 0
                dode = 0
                #print(f"{i},{j}")
                if i == 0:
                    if j == 0: # Øvre venstre hjørne
                        if self.cells[i][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                    elif j == self.bredde-1: # Øvre høyre hjørne
                        if self.cells[i][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                    else: # Øvre rad mellom endene.
                        if self.cells[i][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                elif i == self.hoyde-1:
                    if j == 0: # Nedre venstre hjørne
                        if self.cells[i][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                    elif j == self.bredde-1: # Nedre høyre hjørne
                        if self.cells[i][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                    else: # Nedre rad mellom endene.
                        if self.cells[i][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                else:
                    if j == 0: # Venstre kant
                        if self.cells[i-1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                    elif j == self.bredde-1: # Høyre kant
                        if self.cells[i-1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                    else: # Alle andre celler med 8 naboer
                        if self.cells[i-1][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i-1][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j+1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i+1][j-1].levende:
                            levende += 1
                        else:
                            dode += 1
                        if self.cells[i][j-1].levende:
                            levende += 1
                        else:
                            dode += 1


                # Sjekk de fire reglene for hva som skjer i neste iterasjon.
                if celle.levende:
                    if levende < 2:
                        celle.nesteTilstand = False
                    elif levende == 2 or levende == 3:
                        celle.nesteTilstand = True
                    elif levende > 3:
                        celle.nesteTilstand = False
                else:
                    if levende == 3:
                        celle.nesteTilstand = True
                #print(f"{celle.id}: {celle.levende} -> {celle.nesteTilstand}")