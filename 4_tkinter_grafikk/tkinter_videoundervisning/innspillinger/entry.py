"""
Entry med tkinter
"""
import tkinter as tk
window = tk.Tk()
bredde = 500 # størrelse i pixler
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(background="#FFFFFF") # Bruke web colors, white, black, peachpuff, maroon...

# 1) Lage en header boks
header = tk.Frame(window,
    width = bredde,
    height=100,
    background="dodgerblue"
)
header.pack_propagate(False) # Skrur av at children kan endre rammen.
header.pack() # Legger rammen til vinduet.

# 2) Lage en hovedramme der innhold skal ligge
hovedramme = tk.Frame(window,
    width=bredde,
    height=350,
    background="peachpuff"
)
hovedramme.pack_propagate(False)
hovedramme.pack()

# 3) Lage en footer
footer = tk.Frame(window,
    width=bredde,
    height=50,
    background="chartreuse"
)
footer.pack_propagate(False)
footer.pack()

# 4) Lager to tekstfelt med Label
# a) Uten formattering
tekst1 = tk.Label(header, text="Intro til Tkinter")
tekst1.pack()

# b) Med formattering
tekst2 = tk.Label(hovedramme, 
                  text="Hva heter hovedstaden i Norge?",
                  font=("Times", 25),
                  background="peachpuff",
                  foreground="black"
                  )
tekst2.pack()

# 8) Legger til entry-felt (tekstinput)
svar_boks = tk.Entry(hovedramme, background="white", foreground="black")
svar_boks.pack()


# 5) Legger til knapper
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()

svar_knapp = tk.Button(hovedramme, text="Svar", width=6, height=3) # width = 6 x bredde til 0.
svar_knapp.pack()

utskrift = tk.Label(hovedramme,text="tilbakemelding...", font=("Arial",30))
utskrift.pack()


# 6) Lager funksjoner
ant_likes = 0
fasit = "oslo"
def handle_avslutt(event):
    window.destroy()

def handle_svarknapp(event):
    svar = svar_boks.get()
    if svar.lower() == fasit:
        utskrift["text"] = "Riktig!"
    else:
        utskrift["text"] = f"'{svar}' er feil"

# 7) Binder knappene til funksjoner
avslutt.bind("<Button-1>", handle_avslutt) # Button-1 = venstreklikk
svar_knapp.bind("<Button-1>", handle_svarknapp)


window.mainloop()
