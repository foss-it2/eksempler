"""
Quiz med tkinter
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
tekst1 = tk.Label(header, text="QUIZ med Tkinter")
tekst1.pack()

# b) Med formattering
tekst2 = tk.Label(hovedramme, 
    text="",
    font=("Times", 30),
    background="peachpuff",
    foreground="black"
)
tekst2.pack()

utskrift = tk.Label(hovedramme,
    text="Her kommer svaret...",
    font=("Times", 20),
    background="peachpuff",
    foreground="black"
)


# 5) Legger til knapper
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()

ja_knapp = tk.Button(hovedramme, text="JA", width=6, height=3) # width = 6 x bredde til 0.
ja_knapp.pack()

nei_knapp = tk.Button(hovedramme, text="NEI", width=6, height=3)
nei_knapp.pack()

fortsett_knapp = tk.Button(hovedramme, text="FORTSETT", width=6, height=3)
fortsett_knapp.pack()

utskrift.pack()


# 6) Lager funksjoner
questions = [
    ["Er hovedstaden i Norge Oslo?",True],
    ["Er du en robot?",False],
    ["Kan is smelte?",True]
]
index = 0
tekst2["text"] = questions[index][0]

def handle_avslutt(event):
    window.destroy()

def handle_ja_knapp(event):
    if questions[index][1] == True:
        utskrift["text"] = "Riktig!"
    else:
        utskrift["text"] = "Feil!"

def handle_nei_knapp(event):
    if questions[index][1] == False:
        utskrift["text"] = "Riktig!"
    else:
        utskrift["text"] = "Feil!"


def handle_fortsett_knapp(event):
    global index
    index += 1
    if index >= len(questions):
        utskrift["text"] = "Du har vunnet!"
        index = len(questions) - 1
        return
    utskrift["text"] = "Her kommer svaret..."
    tekst2["text"] = questions[index][0]


# 7) Binder knappene til funksjoner
avslutt.bind("<Button-1>", handle_avslutt) # Button-1 = venstreklikk
ja_knapp.bind("<Button-1>", handle_ja_knapp)
nei_knapp.bind("<Button-1>", handle_nei_knapp)
fortsett_knapp.bind("<Button-1>", handle_fortsett_knapp)


window.mainloop()
