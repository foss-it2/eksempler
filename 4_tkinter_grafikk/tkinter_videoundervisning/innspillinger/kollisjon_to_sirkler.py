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
    def __init__(self,navn, 
                 xpos=canvas_width/2, 
                 ypos=canvas_height/2,
                 delta_x=1,delta_y=0,
                 fill="#ffff00", ouline="#ffff00"):
        self.R = 20  # radius
        self.x = xpos
        self.y = ypos # Plasserer i midten av vinduet
        self.fill = fill
        self.outline = ouline
        self.delta_y = delta_y
        self.delta_x = delta_x
        self.tag = navn
    
    def sjekkKollisjon(self, sirkler):
        """Sjekker kollisjon med alle vegger"""
        global isRunning
        # bunnen
        if self.y + self.R >= canvas_height:
            self.delta_y = -self.delta_y
            # Flytter seg selv HELT vekk fra vegg i tilfelle den setter seg fast.
            self.y = canvas_height - self.R
        # venstre
        if self.x - self.R <= 0:
            self.delta_x = -self.delta_x
            self.x = self.R
        # topp
        if self.y - self.R <= 0:
            self.delta_y = -self.delta_y
            self.y = self.R
        # høyre
        if self.x + self.R >= canvas_width:
            self.delta_x = -self.delta_x
            self.x = canvas_width - self.R
        # Sjekk kollisjon mot alle andre sirkler i listen
        for sirkel in sirkler:
            if sirkel.tag == self.tag:  # Hvis sirkelen som sjekkes er seg selv.
                continue
            if abs(sirkel.x - self.x) <= sirkel.R + self.R:
                print("kollisjon!")
                # Flytt sirklene like langt vekk til hver side før fart settes motsatt.
                self.x -= self.delta_x
                self.delta_x = -self.delta_x
                sirkel.x -= sirkel.delta_x
                sirkel.delta_x = -sirkel.delta_x

    
    def tegnSirkel(self):
        canvas.create_oval(self.x-self.R, self.y-self.R,
                        self.x+self.R, self.y+self.R,
                        fill=self.fill, outline=self.outline, tags=self.tag)


    def fjernSirkel(self):
        canvas.delete(self.tag)
    
    def oppdater(self):
        self.x += self.delta_x
        self.y += self.delta_y


sirkelA = Sirkel("sirkelA",canvas_width/2.5,canvas_height/2,3,0,"yellow","yellow")
sirkelB = Sirkel("sirkelB",3*canvas_width/4,canvas_height/2,-3,0,"deeppink","white")

sirkler = [sirkelA, sirkelB]



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
    # Tegn alle sirkler i listen
    for sirkel in sirkler:
        sirkel.tegnSirkel()
    canvas.after(10)  # venter 100 ms
    canvas.update()
    # Fjern alle sirkler i listen
    for sirkel in sirkler:
        sirkel.fjernSirkel()
        sirkel.oppdater()  # Oppdaterer posisjon og eventuelt fart.
    # Sjekker kollisjon med vegger og med andre sirkler.
    for sirkel in sirkler:
        sirkel.sjekkKollisjon(sirkler)  # Legger ved listen.
    teller += 1
    if teller >= 5000:  # Manuell stans etter n antall frames.
        isRunning = False
        # Tegn alle sirkler i listen
        for sirkel in sirkler:
            sirkel.tegnSirkel()


window.mainloop()
