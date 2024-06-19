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
                   height=canvas_height, background="white")
canvas.pack()


# avsluttknapp
footer = tk.Frame(window)
footer.pack()
startSimulering = tk.Button(footer, text="Start simulering")
startSimulering.pack()
drepCeller = tk.Button(footer, text="Drep alle celler")
drepCeller.pack()
nyttBrett = tk.Button(footer, text="Nytt brett")
nyttBrett.pack()
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()

def handle_start(event):
    global isSimulating
    if isSimulating:
        isSimulating = False
    else:
        isSimulating = True

def handle_drep_celler(event):
    drepAlleCeller()

def handle_nytt_brett(event):
    genererNyttBrett()


def handle_avslutt(event):
    global isRunning
    isRunning = False
    window.destroy()

def handle_klikk(event):
    x = event.x
    y = event.y
    for rad in cells:
        for celle in rad:
            id = celle.isPressed(x,y)
            if id:
                print(id)
                canvas.delete(celle.id)
                celle.tegn(canvas)
            

startSimulering.bind("<Button-1>", handle_start)
drepCeller.bind("<Button-1>", handle_drep_celler)
nyttBrett.bind("<Button-1>", handle_nytt_brett)
avslutt.bind("<Button-1>", handle_avslutt)
canvas.bind("<Button-1>", handle_klikk)


def tegnAlleCeller():
    canvas.delete("celle")
    for rad in cells:
        for celle in rad:
            celle.tegn(canvas)

def fjernAlleCeller():
    """Sletter alle celler"""
    global canvas
    for i in range(HOYDE):
        for j in range(BREDDE):
            celle = cells[i][j]
            canvas.delete(celle.id)
            
def drepAlleCeller():
    """Sletter alle celler"""
    global canvas
    for i in range(HOYDE):
        for j in range(BREDDE):
            celle = cells[i][j]
            celle.levende = False
            celle.nesteTilstand = False
            canvas.delete(celle.id)
            

def genererNyttBrett():
    for i in range(HOYDE):
        for j in range(BREDDE):
            celle = cells[i][j]
            celle.levende = celle.setLevende()
            celle.nesteTilstand = celle.levende
    tegnAlleCeller()
        



# 1) Lager rutenett med brikker
# 2) Legge inn trykkefunksjonalitet
# 3) Animere ved å oppdatere celletilstandene

cells = []
BREDDE = 22
HOYDE = 22
W = 25

# Lager brettet med celler.
for i in range(HOYDE):
    cells.append([])
    for j in range(BREDDE):
        cells[i].append(Celle(f"{i},{j}",(j+1)*W,(i+1)*W,W))

game = Conways(cells,HOYDE,BREDDE)

tegnAlleCeller()
#drepAlleCeller()

# Her animinerer vi
start_tid = time.time()
forrige_tid = time.time()
isRunning = True
isSimulating = False
fps = 8
intervall = 1 / fps
while isRunning:
    if time.time() - forrige_tid >= intervall:
        forrige_tid = time.time()
        if isSimulating:
            fjernAlleCeller()
            game.oppdater()
            tegnAlleCeller()

    # Refresh vindu
    window.update()


window.mainloop()
