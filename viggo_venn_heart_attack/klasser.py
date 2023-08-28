"""
Klasser for spillet space invaders
"""

from random import randint
#from tkinter import PhotoImage # macOS
from PIL import Image, ImageTk

class Spill:
    def __init__(self,hoyde, bredde) -> None:
        self.hoyde = hoyde
        self.bredde = bredde
        self.bunn = hoyde
        self.venstre = 0
        self.hoyre = bredde
        self.topp = 0
        self.aliens = {}    # key=tag: verdi=Alien-objekt
        self.tank = Tank(hoyde, bredde)
    
    def newAlien(self,xpos):
        alien = Alien(self.hoyde,self.bredde,xpos)
        self.aliens[alien.tag] = alien  # legger alien-objektet inn i ordbok med key=alien.tag
        print(self.aliens)

    
    def tegn(self,alienobjekt,tegneflate):
        tegneflate.create_rectangle(alienobjekt.xpos-alienobjekt.bredde/2,
                                    alienobjekt.ypos-alienobjekt.bredde/2,
                                    alienobjekt.xpos+alienobjekt.bredde/2,
                                    alienobjekt.ypos+alienobjekt.bredde/2,
                                    fill=alienobjekt.farge,
                                    tags=alienobjekt.tag
                                    )
    def tegnAlien(self,alien,tegneflate):
        tegneflate.create_image(alien.xpos, alien.ypos, image=alien.img, tags=alien.tag)

    def slettAlt(self,tegneflate):
        tegneflate.delete("tank")
        for key in self.aliens:
            alien = self.aliens[key]
            tegneflate.delete(alien.tag)
        for key in self.tank.kuler:
            kule = self.tank.kuler[key]
            tegneflate.delete(kule.tag)
    
    def slettAlien(self,alienTag,tegneflate):
        print(f"Sletter {alienTag}")
        tegneflate.delete(alienTag)
        if alienTag in self.aliens:
            self.aliens.pop(alienTag)
    
    def slettKule(self,kuleTag,tegneflate):
        print(f"Sletter {kuleTag}")
        tegneflate.delete(kuleTag)
        self.tank.kuler.pop(kuleTag)
        print(f"Ant. kuler igjen: {len(self.tank.kuler)}")
    
    
    def tegnTank(self,tegneflate):
        # Tegner kroppen
        tegneflate.create_rectangle(self.tank.xpos-self.tank.bredde/2,
                                    self.tank.ypos-self.tank.hoyde,
                                    self.tank.xpos+self.tank.bredde/2,
                                    self.tank.ypos+self.tank.hoyde,
                                    fill="#80ff00",
                                    outline="#80ff00",
                                    tags="tank"
                                    )
        # Tegner kanonen
        tegneflate.create_rectangle(self.tank.xpos-self.tank.bredde/10,
                                    self.tank.ypos-self.tank.hoyde*3,
                                    self.tank.xpos+self.tank.bredde/10,
                                    self.tank.ypos+self.tank.hoyde,
                                    fill="#80ff00",
                                    outline="#80ff00",
                                    tags="tank"
                                    )
    
    def tegnSimon(self,tegneflate):
        tegneflate.create_image(self.tank.xpos, self.tank.ypos, image=self.tank.img, tags="tank")
    
    def tegnKule(self,kule,tegneflate):
        tegneflate.create_rectangle(kule.xpos-kule.bredde/2,
                                    kule.ypos-kule.hoyde,
                                    kule.xpos+kule.bredde/2,
                                    kule.ypos+kule.hoyde,
                                    fill="#cdcdcd",
                                    tags=kule.tag
                                    )
    def tegnHjerte(self,kule, tegneflate):
        tegneflate.create_image(kule.xpos, kule.ypos, image=kule.img, tags=kule.tag)

    def kollisjonTank(self,alienobjekt,tank):
        if alienobjekt.ypos + alienobjekt.bredde/2 >= tank.ypos - tank.hoyde/2 \
        and tank.xpos-tank.bredde/2 <= alienobjekt.xpos \
        and alienobjekt.xpos <= tank.xpos+tank.bredde/2 :
            return True
        else:
            return False
    

    def kollisjonKuleAlien(self,kule,alienobjekt):
        if alienobjekt.xpos-alienobjekt.bredde/2 <= kule.xpos <= alienobjekt.xpos + alienobjekt.bredde/2 \
        and alienobjekt.ypos+alienobjekt.hoyde/2 >= kule.ypos:
            return True
        else:
            return False


class Alien:
    teller = 1
    def __init__(self,vindusHoyde,vindusBredde,xpos) -> None:
        #self.xpos = randint(-vindusBredde + 30, vindusBredde - 30)
        self.bredde = 59
        self.hoyde = 90
        self.xpos = xpos
        Alien.teller += 1   # Oppdaterer klassevariabelen så vi lager en unik id for neste alien.
        self.ypos = 50
        self.xfart = 0.1
        self.yfart = 0
        self.steg = 50
        self.tag = f"alien{Alien.teller}"
        self.img = ImageTk.PhotoImage(file="viggo_venn_small.png")
        print(f"lagde alien med tag {self.tag}")



class Tank:
    def __init__(self,vindusHoyde,vindusBredde) -> None:
        #self.bredde = vindusBredde/6
        self.bredde = 57
        #self.hoyde = self.bredde/10
        self.hoyde = 80
        self.xpos = vindusBredde / 2
        self.ypos = vindusHoyde - self.hoyde
        self.kanonfart = 5
        self.kuler = {}
        self.xfart = 3
        self.xmax = vindusBredde
        self.img = ImageTk.PhotoImage(file="simon_cowell_small.png")

    
    def skyt(self):
        kule = Kule(self.xpos, self.ypos - 10, self.kanonfart)
        self.kuler[kule.tag] = kule # legger kulen inn i ordboken
    
    def flytt(self):
        self.xpos += self.xfart
        if self.xpos >= self.xmax - self.bredde/2:
            self.xpos = self.xmax - self.bredde/2
        elif self.xpos <= self.bredde/2:
            self.xpos = self.bredde/2

class Kule:
    """
    Kvadratisk kule som bilde av hjerte.
    """
    teller = 1
    def __init__(self,xpos,ypos,fart) -> None:
        self.xpos = xpos
        self.ypos = ypos
        self.fart = fart
        self.bredde = 30
        self.hoyde = 30
        self.tag = f"kule{Kule.teller}"
        Kule.teller += 1
        self.img = ImageTk.PhotoImage(file="heart_30x30.png")