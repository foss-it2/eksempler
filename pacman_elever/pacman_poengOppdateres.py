import tkinter as tk
from tkinter import PhotoImage
from random import randint

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 600
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
canvas = tk.Canvas(frame2,width=windowWidth,height=windowHeight,background="black")
canvas.pack()
#canvas.create_rectangle(10,10,50,50,fill="chartreuse",
#outline="blue",width=5, tags="firkant")
#canvas.create_oval(50,10,90,50,outline="white")

# Lager poeng
poeng_text = canvas.create_text(windowWidth-100, 20, width=100,fill="#ffffff", text="0 Points",
font=("Some Time Later", 20, "bold"))
level_text = canvas.create_text(100, 20, width=100,fill="#ffffff", text="Level 0",
font=("Some Time Later", 20, "bold"))

# 3) Lag pacman-klassen som har informasjonen om pacman: xpos, ypos, retning etc.
class Pacman:
    def __init__(self): 
        self.R = 20 # radius
        self.farge = "yellow"
        self.x = windowWidth / 2
        self.y = windowHeight / 2
        self.fill = "yellow"
        self.outline = "yellow"
        self.x_retning = 1    # starter mot høyre
        self.y_retning = 0    # ingen y-bevegelse
        self.fart = 5
        self.points = 0
        self.level = 0


pacman = Pacman()


# 4) Animer pacman
def tegnPacman():
    canvas.create_oval(pacman.x-pacman.R,pacman.y-pacman.R,
    pacman.x+pacman.R,pacman.y+pacman.R,
        fill=pacman.fill,outline=pacman.outline,tags="pacman")

def fjernPacman():
    canvas.delete("pacman")

def oppdaterPacman():
    canvas.move("pacman",pacman.fart*pacman.x_retning,pacman.fart*pacman.y_retning)

# Print points
def printPoints():
    canvas.itemconfigure(poeng_text, text=f"{pacman.points} points")
    canvas.itemconfigure(level_text, text=f"Level {pacman.level}")

# 5) Teleporter pacman gjennom veggene
# Sjekker om pacman havner utenfor veggene
def sjekkVegg():
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

window.bind("<Key>",processKeypress)

# 7) Lag frukt-klassen og underklassene. Frukt skal dukke opp tilfeldig.
# liste med bildenavn
# metode som gir tilfeldig fruktbilde
# self.bilde settes til bildet som trekkes tilfeldig
# x, y posisjoner
fruits = []
class Frukt:
    fruktTeller = 1 # klassevariabel for å gi hver frukt sin unike id
    def __init__(self,tidspunkt) -> None:
        self.bilder = [
            "apple_small.png",
            "cherry_small.png",
            "orange_small.png",
            "pineapple_small.png",
            "strawberry_small.png"
        ]
        # Oppgave: Lag tilfeldig posisjon som frukten får. Frukt kan ikke ligge delvis utenfor brettet.
        self.x = randint(2*pacman.R, windowWidth - 2*pacman.R)
        self.y = randint(2*pacman.R, windowHeight - 2*pacman.R)
        self.bilde = PhotoImage(file=self.tilfeldigBilde())
        self.varighet = tidspunkt + randint(1000,3000)
        self.id = "id" + str(Frukt.fruktTeller)
        Frukt.fruktTeller += 1
        canvas.create_image(self.x, self.y, image=self.bilde, tags=self.id)

    def tilfeldigBilde(self):
        indeks = randint(0,len(self.bilder)-1)
        return self.bilder[indeks]


def fjernFrukt(milliseconds):
    deleteList = []
    for i in range(len(fruits)):
        frukt = fruits[i]
        if  milliseconds > frukt.varighet:
            canvas.delete(frukt.id)
            deleteList.append(i)
    for j in range(len(deleteList)-1, -1, -1):
        print(f"j: {j}, {deleteList[j]}")
        fruits.pop(deleteList[j])
    #print(f"len(fruits): {len(fruits)}")   

def kollisjon():
    sletteListe = []
    for i in range(len(fruits)):
        frukt = fruits[i]
        # 1) Her skal logikk som tester kollisjon utføres.
        # Hvis avstand mellom sentrum av frukt og pacman er mindre enn R har vi kollisjon som ser ok ut.
        if abs(pacman.x - frukt.x) <= pacman.R and abs(pacman.y - frukt.y) <= pacman.R:
            print(f"kollisjon: {frukt.id}")
            # 2) Canvas må oppdaters så fruktens bilde også fjernes
            canvas.delete(frukt.id)
            # 3) Ved kollisjon skal frukt fjernes fra listen
            sletteListe.append(i)
            # 4) Pacman får poeng!
            pacman.points += 100
            if pacman.points % 500 == 0:
                pacman.level += 1
            printPoints()
    for index in sletteListe:
        fruits.pop(index)


# avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer,text="Avslutt")
avslutt.pack()

def handle_avslutt(event):
    window.destroy()


avslutt.bind("<Button-1>",handle_avslutt)


# Her animinerer vi
teller = 0
isRunning = True
sleepTime = 10
tegnPacman()
while isRunning == True:
    tegnPacman()
    canvas.after(sleepTime)  # venter i x ms.
    canvas.update()
    fjernPacman()
    pacman.x += pacman.fart * pacman.x_retning
    pacman.y += pacman.fart * pacman.y_retning
    sjekkVegg()
    kollisjon()
    teller += sleepTime
    fjernFrukt(teller)
    if teller % 1000 == 0:
        fruits.append(Frukt(teller))

if isRunning == False:
    tegnPacman()



window.mainloop()
