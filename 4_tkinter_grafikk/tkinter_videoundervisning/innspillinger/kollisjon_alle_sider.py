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
overskrift = tk.Label(header, text="Animasjonsloop")
overskrift.pack()

# 2) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=canvas_width,
                   height=canvas_height, background="black")
canvas.pack()

# 3) Lag sirkel-klassen som har informasjonen om sirkel: xpos, ypos, retning etc.


class Sirkel:
    def __init__(self):
        self.R = 20  # radius
        self.x = windowWidth / 2
        self.y = 2 * self.R # Plasserer litt nedenfor toppen av vinduet
        self.fill = "yellow"
        self.outline = "yellow"
        self.delta_y = 5
        self.delta_x = 5


sirkel = Sirkel()


# 4) Animer sirkel
def tegnSirkel():
    canvas.create_oval(sirkel.x-sirkel.R, sirkel.y-sirkel.R,
                       sirkel.x+sirkel.R, sirkel.y+sirkel.R,
                       fill=sirkel.fill, outline=sirkel.outline, tags="sirkel")


def fjernSirkel():
    canvas.delete("sirkel")


def sjekkKollisjon():
    """Sjekker for kolllisjon med alle sidene i vinduet."""
    # Bunn
    if sirkel.y + sirkel.R >= canvas_height:
        sirkel.delta_y = -sirkel.delta_y
        sirkel.y = canvas_height - sirkel.R*1.01
    # høyre
    if sirkel.x + sirkel.R >= canvas_width:
        sirkel.delta_x = -sirkel.delta_x
        sirkel.x = canvas_width - sirkel.R*1.01
    # topp
    if sirkel.y - sirkel.R <= 0:
        sirkel.delta_y = -sirkel.delta_y
        sirkel.y = sirkel.R*1.01
    # venstre
    if sirkel.x - sirkel.R <= 0:
        sirkel.delta_x = -sirkel.delta_x
        sirkel.x = sirkel.R*1.01

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
    tegnSirkel()
    canvas.after(10)  # venter 100 ms
    canvas.update()
    fjernSirkel()
    sirkel.y += sirkel.delta_y
    sirkel.x += sirkel.delta_x
    print(sirkel.y)
    sjekkKollisjon()
    teller += 1
    if teller >= 2000000:
        isRunning = False
        tegnSirkel()


window.mainloop()
