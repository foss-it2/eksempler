"""
Entry med tkinter
"""
import tkinter as tk
window = tk.Tk()
bredde = 500  # størrelse i pixler
hoyde = 500
window.minsize(bredde, hoyde)
# Bruke web colors, white, black, peachpuff, maroon...
window.configure(background="#FFFFFF")

# 1) Lage en header boks
header = tk.Frame(window,
                  width=bredde,
                  height=100,
                  background="dodgerblue"
                  )
header.pack_propagate(False)  # Skrur av at children kan endre rammen.
header.pack()  # Legger rammen til vinduet.

# 2) Lage en hovedramme der innhold skal ligge
hovedramme = tk.Frame(window,
                      width=bredde,
                      height=350,
                      background="peachpuff"
                      )
hovedramme.pack_propagate(False)
hovedramme.pack(fill=tk.BOTH, expand=True)

# 3) Lage en buffer ramme mellom pack og grid for å beholde midtstillingen
buffer_frame = tk.Frame(hovedramme)
buffer_frame.pack()

# 4) Indre ramme som legger ut med grid.
indre_ramme = tk.Frame(buffer_frame, background="peachpuff")
indre_ramme.grid(row=0, column=0)

# 5) Knapper i grid
btn1 = tk.Button(indre_ramme, text="1", width=3, height=3)
btn2 = tk.Button(indre_ramme, text="2", width=3, height=3)
btn3 = tk.Button(indre_ramme, text="3", width=3, height=3)

btn1.grid(row=1, column=1)
btn2.grid(row=1, column=2)
btn3.grid(row=1, column=3)


window.mainloop()
