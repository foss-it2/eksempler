from tkinter import *

window = Tk()
bredde = 500
hoyde = 400

canvas = Canvas(window,width=bredde,height=hoyde, background="#00679f")
canvas.pack()
x = 350
y = 50
canvas.create_rectangle(x,y,x+100,y+37,outline="white")

bilde = PhotoImage(file="viggo_venn_small.png")
canvas.create_image(50,50,image=bilde,tags="bilde")

teksten = canvas.create_text(50,200,text="Jeg er en tekst!")

def minFun(x):
    print(x)

minus = Button(canvas,text="-",command=lambda: minFun("parameter!"))
canvas.create_window(10, 20, anchor='nw', window=minus)



window.mainloop()
