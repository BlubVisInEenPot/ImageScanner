from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("300x200")

w = ttk.Label(root, text='test', font="50")
w.pack()

menubutton = ttk.Menubutton(root, text="Menu")

menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu

var1 = IntVar(value=1)
var2 = IntVar(value=1)
var3 = IntVar(value=0)

menubutton.menu.add_checkbutton(label="Courses",
                                variable=var1)
menubutton.menu.add_checkbutton(label="Students",
                                variable=var2)
menubutton.menu.add_checkbutton(label="Careers",
                                variable=var3)

print(var1)

menubutton.pack()
root.mainloop()