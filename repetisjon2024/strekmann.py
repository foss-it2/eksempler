import tkinter as tk
import time
import math

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
overskrift = tk.Label(header, text="Akselerasjon")
overskrift.pack()

# 2) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=canvas_width,
                   height=canvas_height, background="black")
canvas.pack()

# 3) Lag strekmann-klassen som har informasjonen om strekmann: xpos, ypos, retning etc.


class Strekmann:
    def __init__(self):
        self.l = 50  # lengde på bein
        self.x = windowWidth / 2
        self.y = 100  # Plasserer litt nedenfor toppen av vinduet
        self.fill = "white"
        self.outline = "white"
        self.vinkel = math.pi/2
    
    def oppdater(self):
        self.vinkel += 0.1
        tegnstrekmann()


strekmann = Strekmann()


# 4) Animer strekmann
def tegnstrekmann():
    canvas.create_rectangle(strekmann.x, strekmann.y,strekmann.x + strekmann.l, strekmann.y + strekmann.l/5,
                            fill=strekmann.fill, outline=strekmann.outline)


def fjernstrekmann():
    canvas.delete("strekmann")



# avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()


def handle_avslutt(event):
    window.destroy()


avslutt.bind("<Button-1>", handle_avslutt)


# Her animinerer vi
isRunning = True
intervall = 0.01
forrige_tid = time.time()
start_tid = time.time()
while isRunning == True:
    if time.time() - forrige_tid >= intervall:
        forrige_tid = time.time()
        fjernstrekmann()
        strekmann.oppdater()
        print(strekmann.vinkel)
        tegnstrekmann()
    
    # En ekstra måte å stoppe på hvis totaltid overskrider en verdi.
    if time.time() - start_tid >= 5:
        isRunning = False
        window.destroy()
    
    # Oppdaterer vinduet
    window.update()

window.mainloop()
