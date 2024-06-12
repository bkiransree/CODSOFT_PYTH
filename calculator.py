import tkinter as tk

# Function to update the display
def button_click(symbol):
    current = display_var.get()
    if symbol == 'C':
        display_var.set('')
    elif symbol == '=':
        try:
            result = eval(current)
            display_var.set(str(result))
        except Exception as e:
            display_var.set("Error")
    else:
        display_var.set(current + symbol)

# Create the main window
root = tk.Tk()
root.title("Virtual Calculator")

# Create a variable to hold the display value
display_var = tk.StringVar()
display_var.set('')

# Create the display
display = tk.Entry(root, textvariable=display_var, font=('Arial', 18), bd=5, insertwidth=4, width=20, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Define button symbols
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Create buttons
for i, row in enumerate(buttons):
    for j, symbol in enumerate(row):
        btn = tk.Button(root, text=symbol, font=('Arial', 14), padx=10, pady=10, command=lambda s=symbol: button_click(s))
        btn.grid(row=i+1, column=j, sticky='nsew')

# Set row and column weights for resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
