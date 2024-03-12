"""
En kloss er spinnvill.

To-do:
Animere

"""

import tkinter as tk  # Import tkinter


# Lag vindu
window = tk.Tk()  # Create a window
windowWidth = 400
windowHeight = 400
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.
# Lag klokke-objekt
canvas = tk.Canvas(window, bg="#2e2e2e", width=400,
                   height=400)    # Lager et canvas-objekt
canvas.pack()    # Legg klokken inn i vinduet


class Firkant:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.l = 10
        self.fart = 10
        self.x_retning = 1
        self.y_retning = 0
        self.x_spiral = 0
        self.y_spiral = 0
        self.posisjon_x = 0
        self.posisjon_y = 0
        self.outline = "#fd6496"

    def tegn(self):
        canvas.create_rectangle(self.x-self.l, self.y-self.l,
                                self.x+self.l, self.y+self.l,
                                outline=self.outline, width=3, tags="firkant")

    def fjern(self):
        canvas.delete("firkant")


firkant = Firkant()
firkant.tegn()

teller = 0
isRunning = True
offset_x = 0 # Avstand for å lage spiral
offset_y = 0
teller = 0
while isRunning == True:
    firkant.tegn()
    canvas.after(10)
    canvas.update()
    firkant.fjern()
    firkant.x += firkant.fart * firkant.x_retning
    firkant.y += firkant.fart * firkant.y_retning
    # Høyre
    if firkant.x+firkant.l >= windowWidth - offset_x:
        firkant.x_retning = 0
        firkant.y_retning = 1
        firkant.x = windowWidth - firkant.l
    # Bunn
    if firkant.y+firkant.l >= windowHeight - offset_y:
        firkant.x_retning = -1
        firkant.y_retning = 0
        firkant.y = windowWidth - firkant.l
    # Venstre
    if firkant.x-firkant.l <= 0 + offset_x:
        firkant.x_retning = 0
        firkant.y_retning = -1
        firkant.x = firkant.l
    # Topp
    if firkant.y-firkant.l <= 0 + offset_y:
        firkant.x_retning = 1
        firkant.y_retning = 0
        firkant.y = firkant.l

    teller += 1
    if teller >= 10000000:
        isRunning = False
        firkant.tegn()



window.mainloop()  # Hovedloopen til programmet
