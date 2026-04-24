from tkinter import *
from tkinter import ttk

def add_item():
    item = entry.get()
    if item:
        listbox.insert(END, item)
        entry.delete(0, END)

def remove_item():
    selection = listbox.curselection()
    if selection:
        listbox.delete(selection)

# Create main window

# Configure main grid


# Title label


# Main content frame

# Create Listbox with scrollbar
listbox = Listbox(main_frame, font=('Arial', 10))
listbox.grid(row=0, column=0, sticky="nsew")

# Vertical scrollbar
scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=listbox.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
listbox.configure(yscrollcommand=scrollbar.set)

# Control frame


# Entry and buttons

# Add some initial items

root.mainloop()