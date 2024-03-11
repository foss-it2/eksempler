import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 800
canvas_height = 500
canvas_width = windowWidth
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.


# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

# 2) Lager en header for overskrift
header = tk.Canvas(canvas_frame, width=windowWidth, height=100)
header.pack()
overskrift = tk.Label(header, text="Kollisjon")
overskrift.pack()




# Lager en NY ramme som selve spill-canvas kan ligge inni.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2, width=canvas_width, height=canvas_height, background="black")
canvas.pack()

# 3) Lag sirkel-klassen som har informasjonen om sirkel: xpos, ypos, retning etc.


class Sirkel:
    def __init__(self):
        self.R = 20  # radius
        self.farge = "yellow"
        self.x = windowWidth / 2
        self.y = 1.5 * 2 * self.R # Plasserer litt nedenfor toppen av vinduet
        self.fill = "yellow"
        self.outline = "yellow"


sirkel = Sirkel()


# 4) Animer sirkel
def tegnSirkel():
    canvas.create_oval(sirkel.x-sirkel.R, sirkel.y-sirkel.R,
                       sirkel.x+sirkel.R, sirkel.y+sirkel.R,
                       fill=sirkel.fill, outline=sirkel.outline, tags="sirkel")


def fjernSirkel():
    canvas.delete("sirkel")

def sjekkKollisjon():
    global isRunning
    if sirkel.y + sirkel.R >= canvas_height:
        isRunning = False
        tegnSirkel()



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
    sirkel.y += 5
    # Sjekker kollisjon med bunnen av vinduet.
    sjekkKollisjon()
    print(sirkel.x)
    teller += 1
    if teller >= 5000:
        isRunning = False
        tegnSirkel()


window.mainloop()
