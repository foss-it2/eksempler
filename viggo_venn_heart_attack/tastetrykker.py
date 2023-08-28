from tkinter import *

window = Tk()

def processKeypress(evt):
    """
    Fanger opp tastetrykk.
    """
    key = evt.keysym
    print(key)

window.bind("<Key>",processKeypress)

window.mainloop()

