import tkinter as tk
from tkinter import messagebox

# Function to update the display when buttons are clicked
def button_click(char):
    current = display.get()
    if char == 'C':
        display.set('')
    elif char == '<-':
        display.set(current[:-1])
    elif char == '=':
        try:
            result = eval(current)
            display.set(result)
        except:
            messagebox.showerror("Error", "Invalid Input")
            display.set('')
    else:
        display.set(current + char)

# Create a basic tkinter window
window = tk.Tk()
window.title('Simple Calculator')

# StringVar to hold the contents of the display
display = tk.StringVar()

# Entry widget to display the calculator input and output
entry = tk.Entry(window, textvariable=display, font=('Arial', 18), bd=10, insertwidth=1, width=25, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons for numbers and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('<-', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('=', 5, 1)
]

# Create buttons in a grid
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(window, text=text, font=('Arial', 18), bd=5, padx=20, pady=20, command=lambda t=text: button_click(t))
        btn.grid(row=row, column=col, columnspan=2)
    else:
        btn = tk.Button(window, text=text, font=('Arial', 18), bd=5, padx=20, pady=20, command=lambda t=text: button_click(t))
        btn.grid(row=row, column=col)

# Start the main tkinter loop
window.mainloop()
