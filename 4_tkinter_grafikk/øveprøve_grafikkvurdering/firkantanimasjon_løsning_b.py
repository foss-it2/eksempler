"""
En kloss er spinnvill.

To-do:
Animere

"""

import tkinter as tk  # Import tkinter


# Lag vindu
window = tk.Tk()  # Create a window
window.geometry('400x400')
# Lag klokke-objekt
canvas = tk.Canvas(window, bg="#2e2e2e", width=400,
                   height=400)    # Lager et canvas-objekt
canvas.pack()    # Legg klokken inn i vinduet


class Firkant:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.l = 10
        self.fart = 3
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
while isRunning == True:
    firkant.fjern()
    canvas.after(10)
    firkant.tegn()
    canvas.update()
    firkant.x += firkant.fart * firkant.x_retning
    firkant.y += firkant.fart * firkant.y_retning
    if firkant.x+firkant.l >= 400-firkant.x_spiral:
        firkant.x_retning = 0
        firkant.y_retning = 1
    if firkant.y+firkant.l >= 400-firkant.y_spiral:
        firkant.x_retning = -1
        firkant.y_retning = 0
    if firkant.x-firkant.l <= 0+firkant.x_spiral:
        firkant.x_retning = 0
        firkant.y_retning = -1
    if firkant.y-firkant.l <= 0+firkant.y_spiral:
        firkant.x_retning = 1
        firkant.y_retning = 0
    if firkant.y == firkant.posisjon_y and firkant.x == firkant.posisjon_x:
        firkant.x_spiral += 20
        firkant.y_spiral += 20
        firkant.posisjon_y += 20
        firkant.posisjon_x += 20

    teller += 1
    if teller >= 10000000:
        isRunning = False
        firkant.tegn()

# Animasjon gjøres her:


window.mainloop()  # Hovedloopen til programmet
