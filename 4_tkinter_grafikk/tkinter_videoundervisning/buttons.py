"""
Button med tkinter
Dokumentasjon: https://realpython.com/python-gui-tkinter/"
"""
import tkinter as tk

window = tk.Tk()  # lager et Tk-objekt fra biblioteket tkinter.
windowWidth = 500   # Størrelse i pixler.
windowHeight = 500
window.minsize(windowWidth, windowHeight)
window.configure(background="#FFFFFF")

# 1) Lage en header boks
header = tk.Frame(window,
    width=500, # størrelse i pixler
    height=100, 
    background="dodgerblue")
header.pack_propagate(False)    # Gjør så innholdet ikke påvirker Frame sin størrelse.
header.pack()  # .pack() legger objektet inn i moren sin.

utskrift = tk.Label(header,text="0", font=("Comic Sans", 20))
utskrift.pack()

# 2) Lage en hovedramme der innhold skal ligge.
hovedramme = tk.Frame(window, width=500, height=350, background="peachpuff")
hovedramme.pack_propagate(False)
hovedramme.pack()  # Rekkefølgen av vinduer er bestemt av koderekkefølgen.

# 3) Lage en footer
footer = tk.Frame(window, width=500, height=50, background="chartreuse")
footer.pack_propagate(False)
footer.pack()

# 4) Lager en knapp for å avslutte appen.
avslutt = tk.Button(
    footer,
    text="Avslutt",
    width=6,
    height=3,
    bg="slategray",
    fg="black",
)
avslutt.pack()

like_button = tk.Button(
    hovedramme,
    text="Like",
    width=3,
    height=3,
    bg="LightSeaGreen",
    fg="black",
)
like_button.pack()

# 5) Variabler
likes = 0
utskrift["text"] = likes
fargeValg = True
farge1 = "peachpuff"
farge2 = "sandybrown"

# 6) Definerer funksjoner
def handle_avslutt(event):
    window.destroy()

def handle_like_button(event):
    global likes # Må henvise til global variabel pga. vi endrer variabelen inni funksjonen.
    likes += 1
    utskrift["text"] = likes

def endreFarge(event):
    global fargeValg
    if fargeValg == True:
        fargeValg = False
        hovedramme["background"] = farge2
    else:
        fargeValg = True
        hovedramme["background"] = farge1

# 7) Binder knapper til funksjoner.
avslutt.bind("<Button-1>", handle_avslutt) # Button-1 = venstreklikk
like_button.bind("<Button-1>", handle_like_button) # Button-1 = venstreklikk
like_button.bind("<Button-2>", endreFarge) # Button-2 = høyreklikk


# Kjører eventloopen til vinduet. MÅ LIGGE NEDERST!
window.mainloop()
