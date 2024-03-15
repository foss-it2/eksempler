import tkinter as tk

window = tk.Tk()
windowWidth = 400
windowHeight = 400

frame1 = tk.Frame(window)
frame1.pack()
overskrift = tk.Label(frame1,text="Spretter",font=("Arial",30))
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
        self.yfart = 0
        self.a = 9.81
        self.delta_t = 10

    def tegn_ball(self):
        canvas.create_oval(ball.x-ball.R,ball.y-ball.R,
            ball.x+ball.R,ball.y+ball.R,
            outline=ball.outline, width=3,tags="ball")
    
    def fjern(self):
        canvas.delete("ball")
    
    def oppdaterFart(self):
        self.yfart = self.yfart + self.a * self.delta_t/1000

def handle_avslutt(event):
    window.destroy()




# Avsluttknapp
footer = tk.Frame(window)
footer.pack()
avslutt = tk.Button(footer,text="Avslutt")
avslutt.pack()
avslutt.bind("<Button-1>",handle_avslutt)
marg = tk.Label(footer, height=2)
marg.pack()

# Lage ball
ball = Ball()
ball.tegn_ball()

# Animere ballen
   
    
    



window.mainloop()
