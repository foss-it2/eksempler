"""
Intro til tkinter gjennomgått 1. feb 2024 med IT2-D.
Dokumentasjon finnes her:
https://realpython.com/python-gui-tkinter/
 
"""
import tkinter as tk

window = tk.Tk()  # lager et Tk-objekt fra biblioteket tkinter.
windowWidth = 500   # Størrelse i "pixler".
windowHeight = 500
window.minsize(windowWidth, windowHeight)
window.configure(background="#FFFFFF")

# 1) Lage en header boks
header = tk.Frame(window)
header.pack()  # .pack() legger objektet inn i moren sin.
# Overskrift
overskrift = tk.Label(header, text="Intro til tkinter", font=("Arial", 30))
overskrift.pack()

# 2) Lage en hovedramme der innhold skal ligge.
hovedramme = tk.Frame(window)
hovedramme.pack()  # Rekkefølgen av vinduer er bestemt av koderekkefølgen.

# 3) Innhold skal være tekst.
tekst = tk.Label(hovedramme)
tekst["text"] = "Husk å sjekke dokumentasjonen her: https://realpython.com/python-gui-tkinter/"
tekst.pack()

# 4) Lage en ny ramme inni hovedrammen og fylle med en annen tekst. Comic sans størrelse 15.

# Kjører eventloopen til vinduet. MÅ LIGGE NEDERST!
window.mainloop()
