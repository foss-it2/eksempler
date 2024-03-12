import tkinter as tk
import time
 

window = tk.Tk()
window.title('Knapp')
window.geometry('200x150')

mellomrom = tk.Label(window, width=5, height=7, text="")
mellomrom.pack()
 
btn = tk.Button(window,text="OK")
btn.pack()

class Knapp:
    def __init__(self) -> None:
        self.antTrykk = 0


def handle_button(evt):
    knapp.antTrykk += 1
    if knapp.antTrykk >= 2:
        btn["text"] = knapp.antTrykk
    else:
        btn["text"] = "Du traff!"
    window["bg"] = "#fedcba"
    mellomrom["bg"] = "#fedcba"


knapp = Knapp()

btn.bind("<Button-1>",handle_button)

window.mainloop()