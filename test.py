import tkinter as tk
# from PIL import ImageTk, Image



def init_tk():

    root = tk.Tk()
    root.title("test app")

    frame = tk.Frame(root)
    frame.grid(row=0, column=0)

    entry = tk.Entry(frame, ) # vid 15:38

    root.mainloop()


#_______________________________________________________________________________________________________________________________________________

init_tk()