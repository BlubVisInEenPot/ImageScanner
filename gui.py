from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("image sorter")

searchDir = ""
sortDir = ""
testDictionary_list = [{"name" : "test1", "size" : 3987 },{"name" : "test2", "size" : 197 },{"name" : "test3", "size" : 481 }]


def openfilename():

    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askdirectory()
    return filename

def open_searchDir():
    global searchDir
    currentDir = entry.get()

    filepath = openfilename()
    if currentDir:
        entry.delete(0, END)
    if filepath:
        entry.insert(END, filepath)

def open_sortDir():
    global sortDir
    currentDir = entry2.get()

    filepath = openfilename()
    if currentDir:
        entry2.delete(0, END)
    if filepath:
        entry2.insert(END, filepath)

def display_photoNames():
    global testDictionary_list
    list = testDictionary_list

    for l in list:
        Listbox.insert(END, list(l)("name"))

display_photoNames()

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

entry_btn = Button(frame, text="select source", font=("System native", 9), command=open_searchDir)
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

entry2 = Entry(frame2)
entry2.grid(row=0, column=0, sticky="ew")

entry2_btn = Button(frame2, text="select destination", font=("System native", 9), command=open_sortDir)
entry2_btn.grid(row=0, column=1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


root.mainloop()