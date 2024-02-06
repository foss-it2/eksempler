"""
Frame med tkinter
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
header.pack()  # .pack() legger objektet inn i moren sin.

# 2) Lage en hovedramme der innhold skal ligge.
hovedramme = tk.Frame(window, width=500, height=350, background="peachpuff")
hovedramme.pack()  # Rekkefølgen av vinduer er bestemt av koderekkefølgen.

# 3) Lage en footer
footer = tk.Frame(window, width=500, height=50, background="chartreuse")
footer.pack()

# Kjører eventloopen til vinduet. MÅ LIGGE NEDERST!
window.mainloop()
