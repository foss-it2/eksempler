"""
Label med tkinter
Dokumentasjon: https://realpython.com/python-gui-tkinter/"
"""
import tkinter as tk

window = tk.Tk()  # lager et Tk-objekt fra biblioteket tkinter.
windowWidth = 500   # Størrelse i pixler.
windowHeight = 500
window.minsize(windowWidth, windowHeight)
window.configure(background="#FFFFFF")

# 1) Lage en hovedramme der innhold skal ligge.
hovedramme = tk.Frame(window, width=500, height=350, background="peachpuff")
hovedramme.pack()

# 2) Lager Label (tekst)
tekst1 = tk.Label(hovedramme, text="Dette er en label.") # NB! Bakgrunnsfargen kommer gjennom.
tekst1.pack()

# 3) Lager label med formattering.
tekst2 = tk.Label(hovedramme, 
    text="Formattert tekst", 
    font=("Times", 30), 
    background="#FFFFFF",
    foreground="LightSlateGray")  # https://en.wikipedia.org/wiki/Web_colors
tekst2.pack()

# 4) Lager label med bredde og høyde
tekst3 = tk.Label(hovedramme, 
                  text="Bredde og høyde satt.",
                  width=15, # bredde er 15 x bredden til default font for "0".
                  height=15 # høyde er 15 x høyden til defulat font "0".
                  )
tekst3.pack()


# Kjører eventloopen til vinduet. MÅ LIGGE NEDERST!
window.mainloop()
