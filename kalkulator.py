import tkinter as tk
window = tk.Tk()
overskrift = tk.Label(text="BASIC kalkulator")
overskrift.pack()

# Lager inputfelt for de to tallene A og B
tallA = tk.Entry()
tallA.pack()
tallB = tk.Entry()
tallB.pack()

# Lager de fire knappene + - * /
pluss = tk.Button(text="+")
pluss.pack()
minus = tk.Button(text="-")
minus.pack()
gange = tk.Button(text="*")
gange.pack()
dele = tk.Button(text="/")
dele.pack()
erLik = tk.Button(text="=")
erLik.pack()
avslutt = tk.Button(text="Avslutt")
avslutt.pack()

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
