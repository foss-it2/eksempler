"""
Eksempel på hvordan lage et grafisk brukergrensesnitt (gui) med tkinter-biblioteket.
"""
import tkinter as tk
#print(help(tk))

window = tk.Tk()
windowWidth = 500
windowHeight = 500
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.
window.configure(background='yellow')


# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack() # .pack() legger objektet inn i mor-objektet slik som for tabeller i html.

# 2) Lager en header med overskrift
header = tk.Canvas(canvas_frame, width=windowWidth, height=10)
header.pack()
overskrift = tk.Label(header,text="Intro til tkinter",font=("Arial",30))
overskrift.pack()
overskrift2 = tk.Label(
    header, text="Husk å sjekke: https://realpython.com/python-gui-tkinter/", font=("Arial", 30))
overskrift2.pack()

# Lager en NY ramme som innholdet kan ligge inni.
frame1 = tk.Frame(window)
frame1.pack()




# Kjører gui sin event loop for å fange opp klikk på knapper etc.
window.mainloop()
