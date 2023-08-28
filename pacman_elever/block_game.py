from tkinter import *
import math
import random
import time


master = Tk()

w = Canvas(master,width=600,height=600)
w.pack()

tileSize = 20

def randomColor():
    r = math.floor(random.random() * 255)
    g = math.floor(random.random() * 255)
    b = math.floor(random.random() * 255)
    return '#%02x%02x%02x' % (r, g, b)

class newElement:
    def __init__(self,x,y):
        x = math.floor(x/tileSize) * tileSize
        y = math.floor(y/tileSize) * tileSize
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.width = tileSize
        self.height = tileSize
        self.id = random.random()
        self.color = randomColor()

elements = []

def mouse(event):
    global mouseX,mouseY
    mouseX,mouseY = event.x,event.y

    canPlace = True

    for y in range(0,len(elements)):
        e = elements[y]
        dx = e.x + e.width/2 - mouseX
        dy = e.y + e.height/2 - mouseY
        if math.sqrt(dx*dx+dy*dy) < 20:
            canPlace = False
            break

    if canPlace:
        elements.append(newElement(mouseX,mouseY))

mouseX = 0
mouseY = 0

w.bind("<B1-Motion>",mouse)

elements.append(newElement(300,50))
elements.append(newElement(300,100))

def collision(rect1,rect2):
   return rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and rect1.y < rect2.y + rect2.height and rect1.height + rect1.y > rect2.y

def distance(rect1,rect2):
    dx = rect1.x - rect2.x
    dy = rect2.y - rect2.y
    return math.sqrt(dx*dx+dy*dy)

lastCall = time.time()

def engine():
    global lastCall
    w.delete("all")

    w.create_line(0,590,600,590)

    for i in range(0,len(elements)):
        e = elements[i]

        gravity = 0.1

        e.vy += gravity

        e.x += e.vx
        e.y += e.vy

        if e.y + e.height >= 590:
            e.y = 590-e.height
            e.vy = 0

        for x in range(0,len(elements)):
            e1 = elements[x]
            if e.id == e1.id or distance(e,e1) > 14.14:
                continue
            col = collision(e,e1)
            if col:
                e.y = e1.y - e1.height
                e.vy = 0

        w.create_rectangle(e.x,e.y,e.x+e.width,e.y+e.height,fill=e.color)

    w.create_text(10,10,anchor=NW,text=len(elements))
    fps = 60
    if time.time() - lastCall != 0:
        fps = round(1/(time.time() - lastCall))
    w.create_text(600,10,anchor=NE,text=fps)

    lastCall = time.time()

    master.after(16,engine)
engine()

mainloop()