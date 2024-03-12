import tkinter as tk

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 800
canvas_height = 500
canvas_width = windowWidth
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.

# 1) Lager en header for overskrift
header = tk.Canvas(frame1, width=windowWidth, height=100)
header.pack()
overskrift = tk.Label(header, text="Kollisjon mellom to sirkler.")
overskrift.pack()

# 2) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=canvas_width,
                   height=canvas_height, background="black")
canvas.pack()

# 3) Lag sirkel-klassen som har informasjonen om sirkel: xpos, ypos, retning etc.


class Sirkel:
    def __init__(self,navn, xpos=canvas_width/2, ypos=canvas_height/2,delta_x=1,delta_y=0):
        self.R = 20  # radius
        self.farge = "yellow"
        self.x = xpos
        self.y = ypos # Plasserer i midten av vinduet
        self.fill = "yellow"
        self.outline = "yellow"
        self.delta_y = delta_y
        self.delta_x = delta_x
        self.navn = navn
    
    def sjekkKollisjon(self):
        """Sjekker kollisjon med alle vegger"""
        global isRunning
        # bunnen
        if self.y + self.R >= canvas_height:
            self.delta_y = -self.delta_y
            # Flytter seg selv HELT vekk fra vegg i tilfelle den setter seg fast.
            self.y = canvas_height - self.R
        # venstre
        elif self.x - self.R <= 0:
            self.delta_x = -self.delta_x
            self.x = self.R
        # topp
        elif self.y - self.R <= 0:
            self.delta_y = -self.delta_y
            self.y = self.R
        # høyre
        elif self.x + self.R >= canvas_width:
            self.delta_x = -self.delta_x
            self.x = canvas_width - self.R


sirkel = Sirkel("sirkel1",canvas_width/4,canvas_height/2)


# 4) Animer sirkel
def tegnSirkel(objekt_tag):
    canvas.create_oval(sirkel.x-sirkel.R, sirkel.y-sirkel.R,
                       sirkel.x+sirkel.R, sirkel.y+sirkel.R,
                       fill=sirkel.fill, outline=sirkel.outline, tags=objekt_tag)


def fjernSirkel(objekt_tag):
    canvas.delete(objekt_tag)


# avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()


def handle_avslutt(event):
    window.destroy()


avslutt.bind("<Button-1>", handle_avslutt)


# Her animinerer vi
teller = 0
isRunning = True
while isRunning == True:
    tegnSirkel(sirkel.navn)
    canvas.after(10)  # venter 100 ms
    canvas.update()
    fjernSirkel(sirkel.navn)
    sirkel.x += sirkel.delta_x
    sirkel.y += sirkel.delta_y
    # Sjekker kollisjon med bunnen av vinduet.
    sirkel.sjekkKollisjon()
    print(sirkel.x)
    teller += 1
    if teller >= 5000:
        isRunning = False
        tegnSirkel(sirkel.navn)


window.mainloop()
