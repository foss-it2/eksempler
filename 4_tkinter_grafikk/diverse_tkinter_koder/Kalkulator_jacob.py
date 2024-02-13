import tkinter as tk
window = tk.Tk()
window.geometry("500x400")
bgcolor = "aquamarine"
window.configure(bg=bgcolor)

overskrift = tk.Label(text="Kalkulator",bg=bgcolor)
overskrift.pack()




# Lager inputfelt for de to tallene A og B
tallA = tk.Entry()
tallA.pack()


frame1 = tk.Frame(window)
frame1.pack()



# Lager de fire knappene + - * /
pluss = tk.Button(frame1, text="+", bg="aquamarine")
pluss.grid(row=2,column=1)

minus = tk.Button(frame1, text="-", background="aquamarine")
minus.grid(row=2,column=2)

gange = tk.Button(frame1,text="x", background="aquamarine")
gange.grid(row=2,column=3)

dele = tk.Button(frame1,text="/", background="aquamarine")
dele.grid(row=2,column=4)



tallB = tk.Entry()
tallB.pack()

frame2 = tk.Frame(window)
frame2.pack()


erLik = tk.Button(frame2,text="=", background="lightgreen")
erLik.grid(row=2,column=1)

avslutt = tk.Button(frame2,text="Avslutt", background="lightcoral")
avslutt.grid(row=2,column=2)

# Verdiene vi jobber med
a = 0
b = 0
operasjon = "pluss"
svar = tk.Label(text=f"Svar")
svar.pack()

def handle_regnUt(event):
    a = float(tallA.get())
    b = float(tallB.get())
    if operasjon == "pluss":
        svar["text"] = a + b
    elif operasjon == "minus":
        svar["text"] = a - b
    elif operasjon == "gange":
        svar["text"] = a * b
    elif operasjon == "dele":
        svar["text"] = a / b

# Programmerer knappene
def handle_pluss(event):
    global operasjon    # kodeordet global forteller funksjonen å bruke variabelen "operasjon" som er definert utenfor.
    operasjon = "pluss"
    
def handle_minus(event):
    global operasjon
    operasjon = "minus"

def handle_gange(event):
    global operasjon
    operasjon = "gange"

def handle_dele(event):
    global operasjon
    operasjon = "dele"

def handle_avslutt(event):
    window.destroy()

# Binder knappene opp mot funksjonene, etter at funksjonene er definert.
pluss.bind("<Button-1>",handle_pluss)
minus.bind("<Button-1>",handle_minus)
gange.bind("<Button-1>",handle_gange)
dele.bind("<Button-1>",handle_dele)
erLik.bind("<Button-1>",handle_regnUt)
avslutt.bind("<Button-1>",handle_avslutt)


# Etter at alt mulig er laget i vinduet kan vi starte programloop
window.mainloop()