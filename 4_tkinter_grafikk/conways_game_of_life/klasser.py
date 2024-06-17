"""
Klasser for simuleringen Conways game of life
"""

class Celle:
    teller = 0
    def __init__(self,x,y,width=5,outline="black",fill="chartreuse") -> None:
        self.w = width
        self.levende = True
        self.outline = outline
        self.fill = fill
        self.x = x
        self.y = y
        self.id = self.settId()
    
    def tegn(self,cnv):
        if self.levende == False:
            self.fill = "grey"
        else:
            self.fill = "chartreuse"
        cnv.create_rectangle(
            self.x - self.w/2,
            self.y - self.w/2,
            self.x + self.w/2,
            self.y + self.w/2,
            fill=self.fill,
            outline=self.outline,
            width=2,
            tags = "celle"
        )
    
    
    def settId(self):
        Celle.teller += 1
        return f"id{Celle.teller}"

    def isPressed(self, x, y):
        # Trekker fra bredden til outline så man ikke kan klikke mellom to celler.
        if self.x+1-self.w/2 <= x <= self.x-1 + self.w/2 and \
            self.y+1-self.w/2 <= y <= self.y-1+self.w/2:
            # Flipper tilstanden levende/død
            self.levende = not self.levende
            return self.id
        else:
            return False