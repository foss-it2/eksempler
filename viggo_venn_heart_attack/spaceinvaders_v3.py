import os
import time
import tkinter as tk


# Import av egne biblioteker
from klasser import *

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 500
windowHeight = 500
window.minsize(windowWidth,windowHeight)    # Setter størrelsen.


# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

# 2) Lager en header med bildet alien
header = tk.Canvas(canvas_frame,width = windowWidth, height = 100)
header.pack()

# Lager en NY ramme som selve spill-canvas kan ligge inni.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2,width=windowWidth,height=windowHeight,background="black")
canvas.pack()


        

# Setter opp piltaster
def processKeypress(evt):
    global spill
    key = evt.keysym
    print(key)
    if key == "Left":
        spill.tank.xfart = -3
    elif key == "Right":
        spill.tank.xfart = 3
    elif key == "space":
        spill.tank.skyt()

window.bind("<Key>",processKeypress)

# Setter opp spillet som igjen lager tanksen.
spill = Spill(windowHeight,windowWidth)
# Lager tre aliens
for i in range(3):
    spill.newAlien()


isRunning = True

teller = 0
isRunning = True
forrige_tid = time.time()

# Kjører koden så fort vi kan og tegner opp ved faste tidsintervaller.
teller = 1
while isRunning:
    teller += 1
    if time.time() - forrige_tid >= 0.01:
        forrige_tid = time.time()
        # 1) slette alt i vinduet, unntatt tanksen.
        spill.slettAlt(canvas)
        # 2) tegn
        # Gå gjennom alle aliens og tegn dem opp
        for key in spill.aliens:
            alien = spill.aliens[key]
            spill.tegn(alien,canvas)
            # Flytt alien
            alien.xpos += alien.xfart
            alien.ypos += alien.yfart
            # 4) Kollisjonstesting
            if spill.kollisjonTank(alien,spill.tank) == True:
                running = False
        # Gå gjennom alle kuler og tegn dem opp
        treff = False
        sletteListe = []
        kulerSomSkalSlettes = []
        for key in spill.tank.kuler:
            if len(sletteListe) > 0:
                break
                #pass
            kule = spill.tank.kuler[key]
            if kule.ypos < 0:
                kulerSomSkalSlettes.append(kule.tag)   # Markerer kule for sletting og går videre til neste kule med "continue"
                print(f"slettet kule {kule.tag}")
                continue
            spill.tegnKule(kule,canvas)
            # Flytt kula
            kule.ypos -= kule.fart
            # Kollisjonstesting mot alle aliens, én etter én.
            alienSkutt = ""
            for key in spill.aliens:
                alien = spill.aliens[key]
                if alien.tag in sletteListe:    # Avbryter å sjekke for treff med flere aliens pga en kule kun kan treffe én alien.
                    print(f"fant {alien.tag} i sletteListen")
                    break   # Avbryter loopen 'for key in spill.aliens'
                if spill.kollisjonKuleAlien(kule,alien) == True:
                    print(f"Kolliderte kule med: {alien.tag}")
                    print(teller)
                    #isRunning = False
                    alienSkutt = alien.tag  # Markerer alien for sletting
                    sletteListe.append(alien.tag)
                    kulerSomSkalSlettes.append(kule.tag)
                    treff = True
                    break
        if treff == True:
            print(sletteListe)
            sletteListe = []
            spill.slettAlien(alienSkutt,canvas)   
        if len(kulerSomSkalSlettes) != 0:
            for kuleTag in kulerSomSkalSlettes:
                spill.slettKule(kuleTag,canvas)
        spill.tegnTank(canvas)
        spill.tank.flytt()
        
        
        
        
    # Oppdaterer vinduet
    window.update()

window.mainloop()






