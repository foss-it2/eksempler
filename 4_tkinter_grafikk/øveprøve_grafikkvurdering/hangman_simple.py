import tkinter as tk
from random import randint

window = tk.Tk()
overskrift = tk.Label(text="Hangman")
overskrift.pack()

label_ord = tk.Label(window, text="Gjett")
label_ord.pack()
entry_ord = tk.Entry()
entry_ord.pack()


div = tk.Frame(window)
div.pack()

knapp = tk.Button(div,text="Gjett")
knapp.grid(column=1,row=1)
fasit = tk.Button(div,text="Fasit")
fasit.grid(column=2,row=1)
utskrift = tk.Label(window, height=10, width=25)
utskrift.pack()

class Hangman:
    def __init__(self) -> None:
        self.ord = ["bok","lampe","saks"]
        self.index= randint(0,len(self.ord)-1)
        self.svar = self.ord[self.index]
        self.antallForsok = 0

# Programmerer knappene
def handle_button(evt):
    # 1) Går gjennom og sjekker om bokstav ligger i ordet
    hangman.antallForsok += 1
    ord = entry_ord.get()
    riktige = {}
    for i in range(len(ord)):
        bokstav = ord[i]
        if not bokstav in riktige:    # Dersom vi ikke har talt bokstaven før setter vi den til 0.
            riktige[bokstav] = 0
            for j in range(len(hangman.svar)):
                if bokstav == hangman.svar[j]:
                    riktige[bokstav] += 1
    if len(riktige) == len(hangman.svar):
        tekst = f"Gratulerer! \n Du klarte det på {hangman.antallForsok} forsøk."
    else:
        tekst = "Du hadde \n"
        for key in riktige:
            tekst += f"{riktige[key]} riktig {key} \n"
    utskrift["text"] = tekst
        


def handle_fasit(evt):
    utskrift["text"] = hangman.svar

knapp.bind("<Button-1>",handle_button)
fasit.bind("<Button-1>",handle_fasit)

# Lager spillet
hangman = Hangman()

# Etter at alt mulig er laget i vinduet kan vi starte programloop
window.mainloop()
