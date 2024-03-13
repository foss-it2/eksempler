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
        self.border = 3
        self.bredde = 2*self.l + 2*self.border
        self.fart = 10
        self.x_retning = 1
        self.y_retning = 0
        self.posisjon_x = 0
        self.posisjon_y = 0
        self.fill = "dodgerblue"
        self.outline = "#fd6496"

    def tegn(self):
        canvas.create_rectangle(self.x-self.l, self.y-self.l,
                                self.x+self.l, self.y+self.l,
                                outline=self.outline,width=self.border, tags="firkant")

    def fjern(self):
        canvas.delete("firkant")


firkant = Firkant()
firkant.tegn()

teller = 0
isRunning = True
teller = 0
while isRunning == True:
    firkant.tegn()
    canvas.after(10)
    canvas.update()
    firkant.fjern()
    firkant.x += firkant.fart * firkant.x_retning
    firkant.y += firkant.fart * firkant.y_retning
    # Høyre
    if firkant.x+firkant.bredde/2 >= canvas_width and firkant.x_retning == 1:
        firkant.x_retning = 0
        firkant.y_retning = 1
        firkant.x = canvas_width - firkant.bredde/2
    # Bunn
    if firkant.y+firkant.bredde/2 >= canvas_height and firkant.y_retning == 1:
        firkant.x_retning = -1
        firkant.y_retning = 0
        firkant.y = canvas_height - firkant.bredde/2
    # Venstre
    if firkant.x-firkant.bredde/2 <= 0 and firkant.x_retning == -1:
        firkant.x_retning = 0
        firkant.y_retning = -1
        firkant.x = firkant.bredde/2
    # Topp
    if firkant.y-firkant.bredde/2 <= 0 and firkant.y_retning == -1:
        firkant.x_retning = 1
        firkant.y_retning = 0
        firkant.y = firkant.bredde/2


    teller += 1
    if teller >= 10000000:
        isRunning = False
        firkant.tegn()



window.mainloop()  # Hovedloopen til programmet
