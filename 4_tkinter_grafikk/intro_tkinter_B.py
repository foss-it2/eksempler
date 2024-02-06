"""
Enkelt eksempel
"""
import tkinter as tk

window = tk.Tk()
bredde = 500
hoyde = 500
window.minsize(bredde, hoyde)
window.configure(background="#FFFFFF")

# Lager en header-ramme
header = tk.Frame(window)
header.pack() # Legger header-objektet inn i window-rammen.
overskrift = tk.Label(header, text="Intro til Tkinter", font=("Arial", 30))
overskrift.pack()

# Lager innholds-ramme
innhold = tk.Frame(window)
innhold.pack()
tekst = tk.Label(innhold, background="#FF3311")
tekst["text"] = "Dokumentasjon ligger her: https://www.geeksforgeeks.org/python-gui-tkinter/"
tekst.pack()

# 1) Lage en ny ramme med valgfri tekst.

# 2) Sett fargen til teksten.

# Starter eventloop for GUI. Må ligge nederst i programmet.
window.mainloop()