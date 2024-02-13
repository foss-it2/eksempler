"""
Button med tkinter
"""
import tkinter as tk
from random import randint
window = tk.Tk()
bredde = 500 # størrelse i pixler
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(background="#FFFFFF") # Bruke web colors, white, black, peachpuff, maroon...

questions = [
    ["Er hovedstaden i Norge Oslo?", True],
    ["Faget vårt heter Norsk", False],
    ["13.02.2024 var en mandag", False]
]

def trekkSpm():
    if len(questions) > 0:
        index = randint(0, len(questions)-1)
        spm = questions[index]
        questions.remove(spm)
        return spm
    else:
        return None


# 1) Lage en header boks
header = tk.Frame(window,
    width = bredde,
    height=100,
    background="cornsilk"
)
header.pack_propagate(False) # Skrur av at children kan endre rammen.
header.pack() # Legger rammen til vinduet.

# 2) Lage en hovedramme der innhold skal ligge
hovedramme = tk.Frame(window,
    width=bredde,
    height=350,
    background="sandybrown"
)
hovedramme.pack_propagate(False)
hovedramme.pack()

# 3) Lage en footer
footer = tk.Frame(window,
    width=bredde,
    height=50,
    background="burlywood"
)
footer.pack_propagate(False)
footer.pack()

# 4) Lager to tekstfelt med Label
# a) Uten formattering
tekst1 = tk.Label(header, text="Quiz")
tekst1.pack()

# b) Med formattering
tekst2 = tk.Label(hovedramme, 
                  text="Her kommer spørsmålet...",
                  font=("Times", 30),
                  background="sandybrown",
                  foreground="black"
                  )
tekst2.pack()


# 5) Legger til knapper
avslutt = tk.Button(footer, text="Avslutt")
avslutt.pack()

like_knapp = tk.Button(hovedramme, text="JA", width=6, height=3) # width = 6 x bredde til 0.
like_knapp.pack()




# 6) Lager funksjoner
def handle_avslutt(event):
    window.destroy()

def handle_like_knapp(event):
    # Hvis JA-trykk
    global spm, poeng
    if spm[1] == True:
        # oppdaterer poeng
        poeng += 1
        # beskjed til bruker
        tekst2["text"] = "JA er riktig!"
    else:
        tekst2["text"] = "JA er feil!"

# 9) Funksjon for NEI-knapp
def handle_dislike(event):
    # Hvis NEI-trykk
    global spm, poeng
    if spm[1] == False:
        # oppdaterer poeng
        poeng += 1
        # beskjed til bruker
        tekst2["text"] = "NEI er riktig!"
    else:
        tekst2["text"] = "NEI er feil!"

def handle_fortsett(event):
    nyttSpm()

spm = ""
poeng = 0

def nyttSpm():
    global spm, poeng
    # Trekker spm
    spm = trekkSpm()
    if spm is not None:
        # Skriver spm på skjerm
        tekst2["text"] = spm[0]
    else:
        tekst2["text"] = f"Ferdig! Poeng: {poeng}"

nyttSpm()

# 7) Binder knappene til funksjoner
avslutt.bind("<Button-1>", handle_avslutt) # Button-1 = venstreklikk
like_knapp.bind("<Button-1>", handle_like_knapp) # Button-3 = høyreklikk windows.

# 8) Lager en senke-knapp (Dislike!)
senkeKnapp = tk.Button(hovedramme, text="NEI!", width=6, height=3)
senkeKnapp.pack()
fortsett_knapp = tk.Button(hovedramme, text="FORTSETT")
fortsett_knapp.pack()

# 9) Bind dislike-knappen til senkefunksjon.
senkeKnapp.bind("<Button-1>", handle_dislike)

fortsett_knapp.bind("<Button-1>", handle_fortsett)


window.mainloop()
