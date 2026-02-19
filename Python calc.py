import tkinter as tk
from tkinter import messagebox

# Colors for the calculator UI (keep these exactly the same)
BG_COLOR = "#121212"
TEXT_COLOR = "#ffffff"
BTN_COLOR = "#2c2c2c"
OP_COLOR = "#3d5afe"
EQUAL_COLOR = "#6200ea"
CLEAR_COLOR = "#cf6679"

# Variables to keep track of what's being typed
current_input = ""
history_text = ""

# This function runs every time a button is clicked
def button_pressed(char):
    global current_input, history_text
    
    # If they click AC, reset everything
    if char == 'AC':
        current_input = ""
        history_text = ""
    # Remove the last character typed
    elif char == 'DEL':
        current_input = current_input[:-1]
    # Calculate the result
    elif char == '=':
        try:
            # Save the current math to the history line
            history_text = current_input + " ="
            
            # eval() calculates the string like it's actual math
            result = eval(current_input)
            current_input = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by zero isn't allowed!")
            current_input = ""
        except:
            # If the math is invalid (like "5++5"), show an error
            messagebox.showerror("Error", "Invalid expression.")
            current_input = ""
    else:
        # If the screen is empty, don't allow starting with a zero unless it's a decimal
        if current_input == "" and char != ".":
            current_input = str(char)
        else:
            current_input += str(char)
            
    # Always update the screen after a click
    refresh_ui()

# Updates the text shown on the calculator
def refresh_ui():
    main_display.delete(0, tk.END)
    # If empty, just show a zero
    text_to_print = current_input if current_input else "0"
    main_display.insert(0, text_to_print)
    
    # Set the history label text
    history_label.config(text=history_text)

# Set up the main window
root = tk.Tk()
root.title("My Python Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# Top label for the history
history_label = tk.Label(root, text="", anchor='e', font=("Arial", 12), bg=BG_COLOR, fg="gray", padx=10)
history_label.pack(fill='both', pady=(10, 0))

# The main number display area
main_display = tk.Entry(root, font=("Arial", 36), borderwidth=0, bg=BG_COLOR, fg=TEXT_COLOR, justify='right')
main_display.pack(fill='both', padx=10, pady=(0, 20))
main_display.insert(0, "0")

# Frame to hold all the buttons
button_grid = tk.Frame(root, bg=BG_COLOR)
button_grid.pack(expand=True, fill='both', padx=10, pady=10)

# List of buttons: (Label, Row, Column, Color)
labels = [
    ('AC', 0, 0, CLEAR_COLOR), ('DEL', 0, 1, BTN_COLOR), ('%', 0, 2, BTN_COLOR), ('/', 0, 3, OP_COLOR),
    ('7', 1, 0, BTN_COLOR),    ('8', 1, 1, BTN_COLOR),    ('9', 1, 2, BTN_COLOR),    ('*', 1, 3, OP_COLOR),
    ('4', 2, 0, BTN_COLOR),    ('5', 2, 1, BTN_COLOR),    ('6', 2, 2, BTN_COLOR),    ('-', 2, 3, OP_COLOR),
    ('1', 3, 0, BTN_COLOR),    ('2', 3, 1, BTN_COLOR),    ('3', 3, 2, BTN_COLOR),    ('+', 3, 3, OP_COLOR),
    ('0', 4, 0, BTN_COLOR),    ('.', 4, 1, BTN_COLOR),    ('=', 4, 2, EQUAL_COLOR)
]

# Create and place each button
for (txt, r, c, clr) in labels:
    # Use lambda to pass the button text to the function
    action = lambda t=txt: button_pressed(t)
    
    # The equals button spans two columns
    w_span = 2 if txt == '=' else 1
    
    btn = tk.Button(button_grid, text=txt, font=("Arial", 14, "bold"), bg=clr, fg=TEXT_COLOR, 
                    borderwidth=0, activebackground="#444444", activeforeground="white", command=action)
    btn.grid(row=r, column=c, columnspan=w_span, sticky="nsew", padx=4, pady=4)

# Make buttons expand to fill the window
for i in range(5): button_grid.rowconfigure(i, weight=1)
for i in range(4): button_grid.columnconfigure(i, weight=1)

# Run the app
root.mainloop()
