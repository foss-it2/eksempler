import tkinter as tk
window = tk.Tk()
header = tk.Frame(window)
header.pack()
overskrift = tk.Label(text="GRID kalkulator")
overskrift.pack()

# Lager en ramme som vi kan putte resten inni
hovedvindu = tk.Frame(window)
hovedvindu.pack()

# Lager inputfelt for de to tallene A og B
tallA = tk.Entry(hovedvindu)    # Legger entryfelt inn i hovedvindu
tallA.grid(row=1,column=1)
tallB = tk.Entry(hovedvindu)
tallB.grid(row=2,column=1)

# Lager de fire knappene + - * / i ny ramme
navigasjon = tk.Frame(window)
navigasjon.pack()

pluss = tk.Button(navigasjon,text="+")
pluss.grid(row=3,column=1)
minus = tk.Button(navigasjon,text="-")
minus.grid(row=3,column=2)

gange = tk.Button(navigasjon, text="*")
gange.grid(row=4, column=1)
dele = tk.Button(navigasjon, text="/")
dele.grid(row=4, column=2)

erLik = tk.Button(navigasjon,text="=")
erLik.grid(row=5,column=2)
avslutt = tk.Button(navigasjon,text="Avslutt")
avslutt.grid(row=6,column=1, columnspan=3)

# Verdiene vi jobber med
a = 0
b = 0
operasjon = "pluss"

# Lager enda en ramme som kan holde sluttsvaret
footer = tk.Frame(window)
footer.pack()
svar = tk.Label(footer,text=f"Svar",font=('Lucida font',20))    # legger label inni footer
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
gange.bind("<Button-1>", handle_gange)
dele.bind("<Button-1>", handle_dele)
erLik.bind("<Button-1>",handle_regnUt)
avslutt.bind("<Button-1>",handle_avslutt)


# Etter at alt mulig er laget i vinduet kan vi starte programloop
window.mainloop()
