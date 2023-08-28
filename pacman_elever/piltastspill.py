import tkinter as tk
import os

window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 550
window.minsize(windowWidth,windowHeight)    # Setter størrelsen.


# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

# 2) Lager en header med bildet ball
header = tk.Canvas(canvas_frame,width = windowWidth, height = 100)
header.pack()

# Lager en NY ramme som selve spill-canvas kan ligge inni.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2,width=windowWidth,height=windowHeight,background="black")
canvas.pack()

# 3) Lag ball-klassen som har informasjonen om ball: xpos, ypos, retning etc.
class Ball:
    def __init__(self): 
        self.R = 10 # radius
        self.farge = "yellow"
        self.x = self.R + 10
        self.y = self.R
        self.fill = "yellow"
        self.outline = "yellow"
        self.x_retning = 1    # starter 1 mot høyre
        self.y_retning = 1    # 1 i y-retning gir skrå fart
        self.fart = 5

ball = Ball()

# Plattform
class Plate:
    def __init__(self) -> None:
        self.x = windowWidth / 2
        self.y = windowHeight - 100
        self.width = 60
        self.height = 10
        self.farge = "white"
        self.fart = 0

plate = Plate()


# 4) Animer ball
def tegnBall():
    canvas.create_oval(ball.x-ball.R,ball.y-ball.R,
    ball.x+ball.R,ball.y+ball.R,
        fill=ball.fill,outline=ball.outline,tags="ball")

def fjernBall():
    canvas.delete("ball")

def tegnPlate():
    canvas.create_rectangle(plate.x - plate.width/2, plate.y - plate.height/2, plate.x + plate.width/2, plate.y + plate.height/2,fill=plate.farge,tags="plate")

def fjernPlate():
    canvas.delete("plate")


# 5) Spretter ball mot vegger
def sjekkVegg():
    if ball.x > windowWidth - ball.R: # Til høyre
        ball.x_retning = -ball.x_retning
    elif ball.x < 0 + ball.R:
        ball.x_retning = -ball.x_retning
    elif ball.y < 0 + ball.R:
        ball.y_retning = -ball.y_retning
    elif ball.y > windowHeight - ball.R:
        ball.y_retning = -ball.y_retning

# 6) Tastaturkontroll med piltaster.
def processKeypress(evt):
    key = evt.keysym
    print(f'Pressed: {key}')
    if key == "Left":
        plate.x -= 10
        if plate.x <= plate.width/2:
            plate.x = plate.width/2
    elif key == "Up":
        plate.y -= 10
        if plate.y <= plate.height/2:
            plate.y = plate.height/2
    elif key == "Right":
        plate.x += 10
        if plate.x >= windowWidth - plate.width/2:
            plate.x = windowWidth - plate.width/2
    elif key == "Down":
        plate.y += 10
        if plate.y >= windowHeight - plate.height/2:
            plate.y = windowHeight - plate.height/2


window.bind("<Key>",processKeypress)


# 7) Kollisjon
# Her må det testes for om ballen har x-pos mellom platens ytterkanter.
# Y-posisjon mellom platens ytterkanter i y-retning.
def kollisjon():
    if ball.x+ball.R >= plate.x-plate.width/2 \
        and ball.x-ball.R <= plate.x+plate.width/2 \
            and ball.y+ball.R > plate.y-plate.height/2 \
                 and ball.y-ball.R < plate.y+plate.height/2:
        ball.y_retning = -ball.y_retning


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
while isRunning == True:
    tegnBall()
    tegnPlate()
    canvas.after(10)  # venter 10 ms
    canvas.update()
    fjernBall()
    fjernPlate()
    ball.x += ball.fart * ball.x_retning
    ball.y += ball.fart * ball.y_retning
    sjekkVegg()
    kollisjon()
    teller += 1

if isRunning == False:
    tegnBall()
    tegnPlate()



window.mainloop()
