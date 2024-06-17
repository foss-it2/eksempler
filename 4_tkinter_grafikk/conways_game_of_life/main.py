import tkinter as tk
import time

from klasser import *

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 700
windowHeight = 700
canvas_height = 600
canvas_width = windowWidth
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.

# 1) Lager en header for overskrift
header = tk.Canvas(frame1, width=windowWidth, height=100)
header.pack()
overskrift = tk.Label(header, text="Conways Game Of Life")
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
    global isRunning
    isRunning = False
    window.destroy()

def handle_klikk(event):
    x = event.x
    y = event.y
    for celle in cells:
        id = celle.isPressed(x,y)
        if id:
            print(id)
    tengAlleCeller(event)
            

avslutt.bind("<Button-1>", handle_avslutt)
window.bind("<Button-1>", handle_klikk)

def tengAlleCeller(event):
    canvas.delete("celle")
    for celle in cells:
        celle.tegn(canvas)

# 1) Lager rutenett med brikker
# 2) Legge inn trykkefunksjonalitet
# 3) Animere ved å oppdatere celletilstandene

cells = []
BREDDE = 22
HOYDE = 22
W = 25

for i in range(1,HOYDE):
    for j in range(1,BREDDE):
        cells.append(Celle(f"id{i},{j}",j*W,i*W,W))

tengAlleCeller(canvas)



# Her animinerer vi
start_tid = time.time()
forrige_tid = time.time()
isRunning = True
fps = 30
intervall = 1 / fps
while isRunning:
    if time.time() - forrige_tid >= intervall:
        forrige_tid = time.time()

    # Refresh vindu
    window.update()


window.mainloop()
