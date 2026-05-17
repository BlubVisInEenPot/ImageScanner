# to do
# settings:
# setting om sorting uit te zetten voor bepaalde cameras
# functions:
# date extractor function
# redo isImage():  ## als je alleen kijkt naar of bijvoorbeeld jpg in de naam zit dan kan je een bestant hebben die bestant.jpg.py heet


from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox
import imagescan

root = Tk()

root.geometry("600x300")
root.minsize(550, 150)
root.title("image sorter")

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

def display_photoNames(list):

    for l in range(0,len(list)):
        listbox.insert(END, list[l]["name"])

updateCounter = 0
def doOnUpdate():
  global root, updateCounter
  updateCounter += 1
  # print(str(updateCounter)+ " folders scanned")
  label.config(text= f"scanned folders: {updateCounter}")
  root.update()

def search_photos():
    directory = entry.get()

    try:
        imagescan.scanFolders(directory, doOnUpdate)  # roep functie aan
        imagescan.imageList.sort(key=imagescan.sortFunc)
    except FileNotFoundError:
        messagebox.showerror(title=None, message="niet gevonden")
    # except PermissionError:
    #     messagebox.showerror(title=None, message="no permision to file")
    except Exception as e:
        print(f"error: {type(e)}")

    display_photoNames(imagescan.imageList)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=0)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_top = Frame(root)
frame_top.grid(row=0, column=0, sticky="ew")
###
# frame_top.columnconfigure(0, weight=0)
# frame_top.columnconfigure(1, weight=1)
# frame_top.columnconfigure(2, weight=1)
# frame_top.columnconfigure(3, weight=0)
# frame_top.rowconfigure(0, weight=0)
###

entry = Entry(frame_top)
entry.pack(side=LEFT, fill=BOTH, expand=True)

button_1 = Button(frame_top, text="select source", font=("System native", 9), command=open_searchDir)
button_1.pack(side=LEFT, expand=False)

entry2 = Entry(frame_top)
entry2.pack(side=LEFT, fill=BOTH, expand=True)

button_2 = Button(frame_top, text="select destination", font=("System native", 9), command=open_sortDir)
button_2.pack(side=LEFT, expand=False)


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_middle = Frame(root)
frame_middle.grid(row=1, column=0, sticky="nsew")
###
frame_middle.columnconfigure(0, weight=1)
frame_middle.columnconfigure(1, weight=1)
frame_middle.rowconfigure(1, weight=1)
###

listbox = Listbox(frame_middle)
listbox.grid(row=1, column=0, sticky="nsew")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_bottom = Frame(root)
frame_bottom.grid(row=2, column=0, sticky="ew") #, columnspan=2, sticky="ew")
###
frame_bottom.columnconfigure(0, weight=1)
frame_bottom.columnconfigure(1, weight=1)
frame_bottom.columnconfigure(2, weight=1)
frame_bottom.rowconfigure(0, weight=0)
###

button_3 = Button(frame_bottom, text="search photos", font=("System native", 9), command=search_photos)
button_3.grid(row=0, column=0, sticky="w")

button_4 = Button(frame_bottom, text="button", font=("System native", 9))
button_4.grid(row=0, column=2, sticky="e")

label = Label(frame_bottom, text= f"scanned folders: {updateCounter}", font=("System native", 9))
label.grid(row=0, column=1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

root.mainloop()