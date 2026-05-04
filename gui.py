from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import imagescan

root = Tk()
root.title("image sorter")

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

    for l in range(0,len(testDictionary_list)):
        listbox.insert(END, testDictionary_list[l]["name"])

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

root.rowconfigure(2, weight=1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_left = Frame(root)
frame_left.grid(row=0, column=0, sticky="nsew")

frame_left.columnconfigure(0, weight=1)
frame_left.rowconfigure(1, weight=1)

entry = Entry(frame_left)
entry.grid(row=0, column=0, sticky="ew")

entry_btn = Button(frame_left, text="select source", font=("System native", 9), command=open_searchDir)
entry_btn.grid(row=0, column=1)

listbox = Listbox(frame_left)
listbox.grid(row=1, column=0, columnspan=2, sticky="nsew")

scrollbar = Scrollbar(frame_left, orient="horizontal", command=listbox.xview)
scrollbar.grid(row=2, column=0, columnspan=2, sticky="ew")
listbox.configure(xscrollcommand=scrollbar.set)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_right = Frame(root)
frame_right.grid(row=0, column=1, sticky="nsew")

frame_right.columnconfigure(0, weight=1)
frame_right.rowconfigure(1, weight=1)

entry2 = Entry(frame_right)
entry2.grid(row=0, column=0, sticky="ew")

entry2_btn = Button(frame_right, text="select destination", font=("System native", 9), command=open_sortDir)
entry2_btn.grid(row=0, column=1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_controll = Frame(root)
frame_controll.grid(row=1, column=0, columnspan=2, sticky="nsew")

frame_controll.columnconfigure(0, weight=1)
frame_controll.columnconfigure(1, weight=1)
frame_controll.rowconfigure(1, weight=1)

entry3_btn = Button(frame_controll, text="go", font=("System native", 9))
entry3_btn.grid(row=0, column=0, sticky="ew")

entry4_btn = Button(frame_controll, text="go", font=("System native", 9))
entry4_btn.grid(row=0, column=1, )

root.mainloop()