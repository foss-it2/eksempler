import tkinter as tk



def step(*event):
    global teller, keysym
    teller += 1
    label['text'] = f"{keysym} {teller}"
    if len(event) != 0:
        keysym = event[0].keysym

    if label._repeat_on:
        root.after(label._repeat_freq, step)


def stop(*event):
    global teller, keysym
    label['text'] = f"{keysym} {teller}"
    if len(event) != 0:
        teller = 0
    if label._repeat_on:
        label._repeat_on = False
        root.after(label._repeat_freq + 1, stop)
    else:
        label._repeat_on = True


if __name__ == '__main__':
    root = tk.Tk()
    windowWidth = 600
    windowHeight = 550
    root.minsize(windowWidth,windowHeight)    # Setter størrelsen.
    label = tk.Label(root, text=0)
    label._repeat_freq = 10
    label._repeat_on = True

    root.bind('<KeyPress>', step)
    root.bind('<KeyRelease>', stop)
    teller = 0
    keysym = "press any key"

    label.pack()
    root.mainloop()