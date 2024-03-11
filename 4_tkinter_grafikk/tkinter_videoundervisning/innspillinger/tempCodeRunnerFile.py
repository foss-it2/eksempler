window = tk.Tk()
frame1 = tk.Frame(window)
frame1.pack()
windowWidth = 600
windowHeight = 800
canvas_height = 500
canvas_width = windowWidth
window.minsize(windowWidth, windowHeight)    # Setter størrelsen.


# 1) Lager en ramme som canvas kan ligge inni
canvas_frame = tk.Frame(window)
canvas_frame.pack()

# 2) Lager en header for overskrift
header = tk.Canvas(canvas_frame, width=windowWidth, height=100)
header.pack()
overskrift = tk.Label(header, text="Animasjonsloop")
overskrift.pack()




# Lager en NY ramme som selve spill-canvas kan ligge inni.
frame2 = tk.Frame(window)
frame2.pack()
canvas = tk.Canvas(frame2, width=canvas_width, height=canvas_height, background="black")
canvas.pack()