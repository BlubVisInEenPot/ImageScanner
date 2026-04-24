from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("image sorter")

def openfilename():

    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askdirectory()
    return filename

def open_folder():
    filepath = openfilename()
    if filepath:
        listbox.insert(END, filepath)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame = Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

entry = Entry(frame)
entry.grid(row=0, column=0, sticky="ew")

entry_btn = Button(frame, text="select folder", command=open_folder)
entry_btn.grid(row=0, column=1)

listbox = Listbox(frame)
listbox.grid(row=1, column=0, columnspan=2, sticky="nsew")

scrollbar = Scrollbar(frame, orient="horizontal", command=listbox.xview)
scrollbar.grid(row=2, column=0, columnspan=2, sticky="ew")
listbox.configure(xscrollcommand=scrollbar.set)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame2 = Frame(root)
frame2.grid(row=0, column=1, sticky="nsew")

frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)

entry = Entry(frame2)
entry.grid(row=0, column=0, sticky="ew")

entry_btn = Button(frame2, text="button")
entry_btn.grid(row=0, column=1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


root.mainloop()