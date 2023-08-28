"""
Space invaders inspirert av Viggo Venn's opptreden på Brittain's Got Talent.
https://www.youtube.com/watch?v=eG7KapXubxU
"""

import os
import time
import tkinter as tk
import threading
from pydub import AudioSegment
from pydub.playback import play


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
header = tk.Canvas(canvas_frame,width = windowWidth, height = 10)
header.pack()

# Lager en NY ramme som selve spill-canvas kan ligge inni.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2,width=windowWidth,height=windowHeight,background="black")
canvas.pack()

# Funksjonen som spiller av lyd n antall ganger.
def thread_function(n):
    song = AudioSegment.from_wav("oneMoreTime_long.wav")
    play(song * n)

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
for i in range(1,8):
    spill.newAlien(i*(50+10))


# Starter sang med threading
x = threading.Thread(target=thread_function, args=(10,))
#x.start()

teller = 0
isRunning = True
forrige_tid = time.time()
alienfart = 0.8
alienTimer = 0

# Kjører koden så fort vi kan og tegner opp ved faste tidsintervaller.
teller = 1
while isRunning:
    teller += 1
    if time.time() - forrige_tid >= 0.01:
        alienTimer += 0.01
        forrige_tid = time.time()
        # 1) slette alt i vinduet, unntatt tanksen.
        spill.slettAlt(canvas)
        # 2) tegn
        # Gå gjennom alle aliens og tegn dem opp
        if alienTimer >= 3:
            for key in spill.aliens:
                alien = spill.aliens[key]
                alien.ypos += alien.hoyde + 5
            alienTimer = 0
            for i in range(1,8):
                spill.newAlien(i*(50+10))
        else:
            for key in spill.aliens:
                alien = spill.aliens[key]
                spill.tegnAlien(alien,canvas)
                # Flytt alien
                alien.xpos += alienfart
                if alien.xpos + alien.bredde/2 >= windowWidth:
                    alienfart = -0.8
                elif alien.xpos - alien.bredde/2 <= 0:
                    alienfart = 0.8
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
            spill.tegnHjerte(kule,canvas)
            #spill.tegnKule(kule,canvas)
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
        spill.tegnSimon(canvas)
        #spill.tegnTank(canvas)
        spill.tank.flytt()
        
        
        
        
    # Oppdaterer vinduet
    window.update()

window.mainloop()






