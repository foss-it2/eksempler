import tkinter as tk
import time

from klasser import *

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
overskrift = tk.Label(header, text="Pactroll")
overskrift.pack()

# 2) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

canvas = tk.Canvas(canvas_frame, width=canvas_width,
                   height=canvas_height, background="black")
canvas.pack()





# avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()


def handle_avslutt(event):
    window.destroy()


def processKeypress(evt):
    global spill
    key = evt.keysym
    print(f'key: {key}')
    spill.handleKeys(key)
    


window.bind("<Key>", processKeypress)

avslutt.bind("<Button-1>", handle_avslutt)

# 1) Lager en brikke
# 2) Lage spill, fylles med brikke(r)
# 3) Animere

brikke1 = Brikke(30,30,50,100)
brikke2 = Brikke(30,30,50,150)
brikke3 = Brikke(30,30,50,20)
brikke3.tekst="H"
brikke3.farge = "grey"
spill = Spill(canvas_width, canvas_height,[brikke1, brikke2, brikke3],canvas)

spill.oppdater()

# Her animinerer vi
start_tid = time.time()
forrige_tid = time.time()
isRunning = True
fps = 30
intervall = 1 / fps
while isRunning:
    if time.time() - forrige_tid >= intervall:
        forrige_tid = time.time()
        isRunning = spill.oppdater()
        

        

    # Refresh vindu
    window.update()



window.mainloop()
