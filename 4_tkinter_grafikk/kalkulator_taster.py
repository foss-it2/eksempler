import tkinter as tk


def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))


def clear():
    entry.delete(0, tk.END)


def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


# Opprett hovedvinduet
root = tk.Tk()
root.title("Kalkulator")

# Opprett en Entry-widget for å vise input og resultater
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Funksjonene for knappene


def create_button_click_func(number):
    return lambda: button_click(number)


def create_operator_click_func(operator):
    return lambda: button_click(operator)


# Opprett knapper for tallene 0-9
buttons = []
for i in range(9):
    button = tk.Button(root, text=str(i+1), padx=10, pady=5)
    button.grid(row=i//3+1, column=i % 3)
    button.config(command=create_button_click_func(i+1))
    buttons.append(button)

button_0 = tk.Button(root, text="0", padx=10, pady=5)
button_0.grid(row=4, column=1)
button_0.config(command=create_button_click_func(0))
buttons.append(button_0)

# Opprett operatørknapper og funksjonsknapper
button_add = tk.Button(root, text="+", padx=10, pady=5)
button_add.grid(row=5, column=3)
button_add.config(command=create_operator_click_func("+"))
button_subtract = tk.Button(root, text="-", padx=10, pady=5)
button_subtract.grid(row=4, column=3)
button_subtract.config(command=create_operator_click_func("-"))
button_multiply = tk.Button(root, text="*", padx=10, pady=5)
button_multiply.grid(row=3, column=3)
button_multiply.config(command=create_operator_click_func("*"))
button_divide = tk.Button(root, text="/", padx=10, pady=5)
button_divide.grid(row=2, column=3)
button_divide.config(command=create_operator_click_func("/"))

button_clear = tk.Button(root, text="C", padx=10, pady=5)
button_clear.grid(row=5, column=1)
button_clear.config(command=clear)
button_equals = tk.Button(root, text="=", padx=10, pady=5)
button_equals.grid(row=5, column=2)
button_equals.config(command=calculate)

# Start hovedloopen
root.mainloop()
