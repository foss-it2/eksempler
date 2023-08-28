# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

# Create a canvas widget
canvas=Canvas(win, width=700, height=350)
canvas.pack()

# Load the image
img=ImageTk.PhotoImage(file="simon_cowell_small.png")

# Add the image in the canvas
canvas.create_image(350, 200, image=img, anchor="center")

win.mainloop()