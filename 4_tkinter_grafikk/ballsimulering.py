import tkinter as tk
import time

window = tk.Tk()
windowWidth = 400
windowHeight = 400

frame1 = tk.Frame(window)
frame1.pack()
overskrift = tk.Label(frame1,text="Ballsimulering",font=("Arial",30))
overskrift.grid(row=1,column=1)


# Lager ramme og canvas.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2,width=windowWidth,height=windowHeight,background="#3e3e3e")
canvas.pack()

class Ball:
    def __init__(self) -> None:
        self.x = windowWidth/2
        self.y = windowHeight/3
        self.R = 10
        self.outline = "#eeeeee"
        self.xfart = 0
        self.yfart = 100
        self.vind = 0
        self.g = 1
        self.tap = 0.85 # Vekstfaktor for hvor mye som tapes i hvert sprett.
        self.ay = self.g * 9.81 * 100   # Ganger med 100 for å få det fra meter til pixler. Så 100 px/s^2.
        self.ax = self.vind * 100
        self.delta_t = 0.01
        self.maksfart = 0

    def tegn_ball(self):
        canvas.create_oval(ball.x-ball.R,ball.y-ball.R,
            ball.x+ball.R,ball.y+ball.R,
            outline=ball.outline, width=3,tags="ball")
    
    def fjern(self):
        canvas.delete("ball")
    
    def oppdaterVind(self):
        self.ax = self.vind * 100

    def oppdaterG(self):
        self.ay = self.g * 9.81 * 100

    def oppdaterFart(self):
        self.yfart = self.yfart + (self.ay * self.delta_t)
        # Oppdaterer maksimal fart for hvert sprett.
        if abs(self.yfart) > self.maksfart:
            self.maksfart = abs(self.yfart)
        self.y += self.yfart * self.delta_t
        if self.y + self.R >= windowHeight:
            self.yfart = -self.yfart*self.tap
            self.y = windowHeight - self.R - 1/100
            print(self.maksfart)
            self.maksfart = 0   # Resetter maksfart for hvert sprett
        self.xfart = self.xfart + (self.ax * self.delta_t)
        self.x += self.xfart * self.delta_t
        if self.x + self.R >= windowWidth:
            self.x = windowWidth - self.R
            self.xfart = -self.xfart*self.tap
        elif self.x + self.R <= 0:
            self.x = self.R
            self.xfart = -self.xfart*self.tap


def handle_start():
    global isRunning
    isRunning = True
    simulering()

def endreVind(operasjon):
    global leftCanvas, ball, vindTekst
    if operasjon == "+":
        ball.vind += 1
        if ball.vind >= 9:
            ball.vind = 9
    else:
        ball.vind -= 1
        if ball.vind <= -9:
            ball.vind = -9
    ball.oppdaterVind()
    leftCanvas.itemconfigure(vindTekst, text=f"{ball.vind} m/s2")
    print(f"vind: {ball.vind}")


def endreGravitasjon(operasjon):
    global leftCanvas, ball, gravTekst
    if operasjon == "+":
        ball.g += 0.5
        if ball.g >= 9:
            ball.g = 9
    else:
        ball.g -= 0.5
        if ball.g <= 0.5:
            ball.g = 0.5
    ball.oppdaterG()
    leftCanvas.itemconfigure(gravTekst, text=f"{ball.g:.1f} G")
    print(f"gravitasjon: {ball.g}")

# GUI
# Footer deles i venstre og høyre del
footer = tk.Frame(window)
footer.pack()

# Lager canvas for å flytte knapper dit jeg vil.
leftCanvas = tk.Canvas(footer)
leftCanvas.pack()

# Lager minus og pluss knapper for vind
minus = tk.Button(leftCanvas,text="<--",command=lambda: endreVind("-"))
leftCanvas.create_window(10, 20, anchor='nw', window=minus)

pluss = tk.Button(leftCanvas,text="-->",command=lambda: endreVind("+"))
leftCanvas.create_window(140, 20, anchor='nw', window=pluss)

vindTekst = leftCanvas.create_text(100, 37,fill="#eeeeee", text="0 m/s2",
    font=("Arial", 14, "bold"))

# Lager minus og pluss knapper for gravitasjon
minusG = tk.Button(leftCanvas,text="<--",command=lambda: endreGravitasjon("-"))
leftCanvas.create_window(10, 70, anchor='nw', window=minusG)

plussG = tk.Button(leftCanvas,text="-->",command=lambda: endreGravitasjon("+"))
leftCanvas.create_window(140, 70, anchor='nw', window=plussG)

gravTekst = leftCanvas.create_text(100, 87,fill="#eeeeee", text="1 G",
    font=("Arial", 14, "bold"))

startKnapp = tk.Button(leftCanvas,text="Start",width=5, height=5, command=handle_start)
leftCanvas.create_window(210, 20, anchor='nw', window=startKnapp)



# Lage ball
ball = Ball()
ball.tegn_ball()
isRunning = False

def simulering():
    global ball, canvas, isRunning
    # Animere ballen
    forrige_tid = time.time()
    while isRunning:
        if time.time() - forrige_tid >= ball.delta_t:
            forrige_tid = time.time()
            ball.fjern()
            ball.tegn_ball()

            ball.oppdaterFart()
            
            # Hvi ballen er nesten på bunnen av vinduet på vei nedover med svært lav fart stopper vi den.
            if ball.yfart <= 10 and ball.yfart > 0 and ball.y >= windowHeight - ball.R - 1 :
                isRunning = False
                print(f"ballfart: {ball.yfart}")
                ball.g = 0
                ball.yfart = 0
                ball.y = windowHeight-ball.R
                ball.fjern()
                ball.tegn_ball()

        canvas.update()



    



window.mainloop()
