"""
En kloss er spinnvill.

To-do:
Animere

"""

import tkinter as tk # Import tkinter
import time


# Lag vindu
window = tk.Tk() # Create a window
window.title("Spiral") # Set title
window.geometry('400x400')
# Lag klokke-objekt
canvas = tk.Canvas(window, bg="#2e2e2e", width=400, height=400)    # Lager et canvas-objekt
canvas.pack()    # Legg klokken inn i vinduet

class Firkant:
    def __init__(self) -> None:
        self.x = 20
        self.y = 20
        self.l = 10
        self.outline = "#fd6496"
        self.retning = 1
    
    def tegn(self):
        canvas.create_rectangle(self.x-self.l,self.y-self.l,
            self.x+self.l,self.y+self.l,
            outline=self.outline, width=3,tags="firkant")

    def oppdater(self):
        self.x += self.retning * 7

    
    def fjern(self):
        canvas.delete("firkant")

firkant = Firkant()
firkant.tegn()

# Animasjon gjøres her:
lastTime = time.time()
teller =0
while True:
    currentTime = time.time()
    if currentTime - lastTime >= 0.01:
        #print(currentTime-lastTime)
        firkant.fjern()
        firkant.oppdater()
        firkant.tegn()
        canvas.update()
        lastTime = time.time()
        teller += 1
        if teller >= 50:
            teller = 0
            firkant.retning = -firkant.retning



window.mainloop() # Hovedloopen til programmet



