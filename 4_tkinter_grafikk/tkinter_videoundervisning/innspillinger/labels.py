"""
Label med tkinter
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
                  text="Formattert tekst",
                  font=("Times", 30),
                  background="peachpuff",
                  foreground="black"
                  )
tekst2.pack()

tekst3 = tk.Label(footer,
                  text="Foooter",
                  font=("Arial", 20),
                  background="maroon",
                  foreground="white"
                  )
tekst3.pack()


window.mainloop()
