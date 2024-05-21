import tkinter as tk

# Function to be called on key press


def on_key_press(event):
    key_symbol = event.keysym
    print(f"Key pressed: {key_symbol}")


# Create the main window
root = tk.Tk()
root.title("Key Press Example")
root.geometry("400x300")

# Label to display instructions
label = tk.Label(root, text="Press any key on your keyboard",
                 font=("Arial", 14))
label.pack(pady=20)

# Bind key press event to the on_key_press function using a lambda
root.bind('<KeyPress>', lambda event: on_key_press(event))

# Run the application
root.mainloop()
