import tkinter as tk

# Define the callback function that runs when the button is clicked
def on_click():
    print("Button was clicked!")

variable = True
def able():
    global variable
    if variable:
        button.config(state="disabled")
        variable = False
    else:
        button.config(state="active")
        variable = True

# 1. Create the main application window
root = tk.Tk()
root.title("Tkinter Button Example")
root.geometry("300x200")

# 2. Create the button widget
# Note: Pass the function name to 'command' WITHOUT parentheses
button = tk.Button(root, text="Click Me", command=on_click)
button.pack(pady=20)
button2 = tk.Button(root, text="disable/enable", command=able)
button2.pack(pady=20)
# 3. Position the button inside the window


# 4. Start the application event loop
root.mainloop()
