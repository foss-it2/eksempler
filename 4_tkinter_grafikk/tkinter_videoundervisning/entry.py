"""
Entry med tkinter
Dokumentasjon: https://realpython.com/python-gui-tkinter/"
"""
import tkinter as tk
from tkmacosx import Button as macButton

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

# 2) Lage en hovedramme der innhold skal ligge.
hovedramme = tk.Frame(window, width=500, height=350, background="peachpuff")
hovedramme.pack_propagate(False)
hovedramme.pack()  # Rekkefølgen av vinduer er bestemt av koderekkefølgen.

utskrift = tk.Label(hovedramme, text="Hva er hovedstaden i Norge?", font=("Arial", 20), background="peachpuff", foreground="black")
utskrift.pack()

# 3) Lage en footer
footer = tk.Frame(window, width=500, height=50, background="chartreuse")
footer.pack_propagate(False)
footer.pack()

# 4) Lager knapper
avslutt = tk.Button(
    footer,
    text="Avslutt",
    width=6,
    height=3,
    bg="slategray",
    fg="black",
)
avslutt.pack()

svar_button = tk.Button(
    hovedramme,
    text="Svar",
    width=3,
    height=3,
    bg="lime",
    fg="black",
)

# 5) Entry felt
svarfelt = tk.Entry(hovedramme, 
    width=50,
    foreground="black",
    background="white",
    )
svarfelt.pack()
svar_button.pack() # Plasserer knappen under svarfeltet.


# 6) Variabler
fasit = "oslo"


# 7) Definerer funksjoner
def handle_avslutt(event):
    window.destroy()

def handle_svar_button(event):
    svar = svarfelt.get()
    if svar.lower() == fasit:
        utskrift["text"] = "Riktig!"
    else:
        utskrift["text"] = f"'{svar}' er feil :("


# 8) Binder knapper til funksjoner.
avslutt.bind("<Button-1>", handle_avslutt) # Button-1 = venstreklikk
svar_button.bind("<Button-1>", handle_svar_button)


# Kjører eventloopen til vinduet. MÅ LIGGE NEDERST!
window.mainloop()
