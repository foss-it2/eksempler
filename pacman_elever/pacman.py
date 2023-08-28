import tkinter as tk
from tkinter import PhotoImage

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 800
window.minsize(windowWidth,windowHeight)    # Setter størrelsen.

#overskrift = tk.Label(frame1,text="Pacman",font=("Arial",30))
#overskrift.grid(row=1,column=1)

# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

# 2) Lager en header med bildet pacman
header = tk.Canvas(canvas_frame,width = windowWidth, height = 100)
header.pack()
# # Load the image
# from PIL import Image, ImageTk
# image=Image.open('pacman_logo_small.png')
# # Resize the image in the given (width, height)
# img=image.resize((windowWidth, 100))
# pacman_logo = ImageTk.PhotoImage(img)
pacman_logo = PhotoImage(file="pacman_logo_small.png")
logo = header.create_image(windowWidth/2,45,image=pacman_logo)



# Lager en NY ramme som selve spill-canvas kan ligge inni.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2,width=windowWidth,height=500,background="black")
canvas.pack()
#canvas.create_rectangle(10,10,50,50,fill="chartreuse",
#outline="blue",width=5, tags="firkant")
#canvas.create_oval(50,10,90,50,outline="white")

# 3) Lag pacman-klassen som har informasjonen om pacman: xpos, ypos, retning etc.
class Pacman:
    def __init__(self): 
        self.R = 20 # radius
        self.farge = "yellow"
        self.x = windowWidth / 2
        self.y = windowHeight / 2
        self.fill = "yellow"
        self.outline = "yellow"

pacman = Pacman()


# 4) Animer pacman
def tegnPacman():
    canvas.create_oval(pacman.x-pacman.R,pacman.y-pacman.R,
    pacman.x+pacman.R,pacman.y+pacman.R,
        fill=pacman.fill,outline=pacman.outline,tags="pacman")

def fjernPacman():
    canvas.delete("pacman")



#fjernPacman()

# 5) Teleporter pacman gjennom veggene

# 6) Tastaturkontroll med piltaster.

# 7) Lag frukt-klassen og underklassene. Frukt skal dukke opp tilfeldig.
# liste med bildenavn
# metode som gir tilfeldig fruktbilde
# self.bilde settes til bildet som trekkes tilfeldig
# x, y posisjoner

def tegn_ball():
    """Tegner en ball i canvas"""


# avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer,text="Avslutt")
fjern_firkant = tk.Button(footer,text="Fjern firkant")
avslutt.pack()
fjern_firkant.pack()

def handle_avslutt(event):
    window.destroy()

def handle_firkant(event):
    canvas.delete("firkant")

avslutt.bind("<Button-1>",handle_avslutt)
fjern_firkant.bind("<Button-1>",handle_firkant)


# Her animinerer vi
teller = 0
isRunning = True
while isRunning == True:
    tegnPacman()
    canvas.after(1000)  # venter 1000 ms
    canvas.update()
    fjernPacman()
    pacman.x += 15
    print(pacman.x)
    teller += 1
    if teller >= 5:
        isRunning = False



window.mainloop()
