import tkinter as tk

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 700
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.


# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

# 2) Lager en header med bildet pacman
header = tk.Canvas(canvas_frame, width=windowWidth, height=100)
header.pack()


# Lager en NY ramme som selve spill-canvas kan ligge inni.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2, width=windowWidth, height=550, background="black")
canvas.pack()

# 3) Lag pacman-klassen som har informasjonen om pacman: xpos, ypos, retning etc.
class Pacman:
    def __init__(self):
        self.R = 20  # radius
        self.farge = "yellow"
        self.x = windowWidth / 2
        self.y = windowHeight / 2
        self.fill = "yellow"
        self.outline = "yellow"
        self.x_retning = 1    # starter mot høyre
        self.y_retning = 0    # ingen y-bevegelse
        self.fart = 5


pacman = Pacman()


# 4) Animer pacman
def tegnPacman():
    canvas.create_oval(pacman.x-pacman.R, pacman.y-pacman.R,
                       pacman.x+pacman.R, pacman.y+pacman.R,
                       fill=pacman.fill, outline=pacman.outline, tags="pacman")


def fjernPacman():
    canvas.delete("pacman")


# 5) Teleporter pacman gjennom veggene

# 6) Tastaturkontroll med piltaster.
def processKeypress(evt):
    key = evt.keysym
    print(f'key: {key}')
    if key == "Left":
        pacman.x_retning = -1
        pacman.y_retning = 0
    elif key == "Up":
        pacman.x_retning = 0
        pacman.y_retning = -1
    elif key == "Right":
        pacman.x_retning = 1
        pacman.y_retning = 0
    elif key == "Down":
        pacman.x_retning = 0
        pacman.y_retning = 1


window.bind("<Key>", processKeypress)


def tegn_ball():
    """Tegner en ball i canvas"""


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
    tegnPacman()
    canvas.after(10)  # venter 10 ms
    canvas.update()
    fjernPacman()
    pacman.x += pacman.fart * pacman.x_retning
    pacman.y += pacman.fart * pacman.y_retning
    # SJEKKER OM pacman er utenfor vinduet
    if pacman.x > windowWidth + pacman.R:
        # Setter ny posisjon
        pacman.x = 0 - pacman.R
    elif pacman.x < 0 - pacman.R:
        pacman.x = windowWidth + pacman.R
    elif pacman.y < 0 - pacman.R:
        pacman.y = windowHeight + pacman.R
    elif pacman.y > windowHeight + pacman.R:
        pacman.y = 0 - pacman.R

    teller += 1
    if teller >= 1000:
        isRunning = False
        tegnPacman()


window.mainloop()
