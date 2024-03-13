"""
En kloss er spinnvill.

To-do:
Animere

"""

import tkinter as tk  # Import tkinter


# Lag vindu
window = tk.Tk()  # Create a window
window.title("Spiral")  # Set title
window.geometry('400x400')
# Lag klokke-objekt
canvas = tk.Canvas(window, bg="#2e2e2e", width=400,
                   height=400)    # Lager et canvas-objekt
canvas.pack()    # Legg klokken inn i vinduet
canvas_width = 400
canvas_height = 400


class Firkant:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.l = 10
        self.fart = 20
        self.x_retning = 1
        self.y_retning = 0
        self.posisjon_x = 0
        self.posisjon_y = 0
        self.fill = "dodgerblue"
        self.outline = "#fd6496"

    def tegn(self):
        canvas.create_rectangle(self.x-self.l, self.y-self.l,
                                self.x+self.l, self.y+self.l,
                                outline=self.outline,width=3, tags="firkant")

    def fjern(self):
        canvas.delete("firkant")


firkant = Firkant()
firkant.tegn()

teller = 0
isRunning = True
offset_x = 20 # Avstand for å lage spiral
offset_y = 20
teller = 0
høyreOffset = 0
bunnOffset = 0
venstreOffset = 0
toppOffset = 0
while isRunning == True:
    firkant.tegn()
    canvas.after(10)
    canvas.update()
    firkant.fjern()
    firkant.x += firkant.fart * firkant.x_retning
    firkant.y += firkant.fart * firkant.y_retning
    # Høyre
    if firkant.x+firkant.l >= canvas_width - høyreOffset and firkant.x_retning == 1:
        firkant.x_retning = 0
        firkant.y_retning = 1
        firkant.x = canvas_width - firkant.l - høyreOffset
        høyreOffset += offset_x
    # Bunn
    if firkant.y+firkant.l >= canvas_height - bunnOffset and firkant.y_retning == 1:
        firkant.x_retning = -1
        firkant.y_retning = 0
        firkant.y = canvas_height - firkant.l - bunnOffset
        bunnOffset += offset_y
    # Venstre
    if firkant.x-firkant.l <= venstreOffset and firkant.x_retning == -1:
        firkant.x_retning = 0
        firkant.y_retning = -1
        firkant.x = firkant.l + venstreOffset
        venstreOffset += offset_x
    # Topp
    if firkant.y-firkant.l <= toppOffset and firkant.y_retning == -1:
        firkant.x_retning = 1
        firkant.y_retning = 0
        firkant.y = firkant.l + toppOffset
        toppOffset += offset_y
    # Sjekker om firkanten har nådd omtrentlig sentrum
    print(f"høyreOffset,toppOffset {høyreOffset},{toppOffset}")
    if 0.98*høyreOffset > canvas_width/2:
        isRunning = False
        firkant.tegn()

    teller += 1
    if teller >= 10000000:
        isRunning = False
        firkant.tegn()



window.mainloop()  # Hovedloopen til programmet
