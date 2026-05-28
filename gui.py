from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox, Tk
import imagescan
from threading import Thread

root = Tk()

root.geometry("600x300")
root.minsize(550, 150)
root.title("image sorter")
# root.iconbitmap("icon.ico")

searchDirectory = r"C:\Users\morten.goudswaard\Downloads"

deleteDubbels_setting = BooleanVar()
deleteDubbels_setting.set(True)
coruptFiles_setting = BooleanVar()
coruptFiles_setting.set(False)
settings_window = None

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
    listbox.delete(0, END)
    for l in range(0,len(list)):
        if len(list[l]['name']) > 23:
            displayName = list[l]['name'][:22] + "..."
        else:
            displayName = list[l]['name']

        listbox.insert(END, f"{displayName:<25}  {list[l]['destFolder']}")

# updateCounter = 0
# def doOnUpdate():
#   global root, updateCounter
#   updateCounter += 1
#   # print(str(updateCounter)+ " folders scanned")
#   label.config(text= f"scanned folders: {updateCounter}")
#   root.update()

def search_photos(event=None):
    global searchDirectory, updateCounter, running
    searchDirectory = entry.get()
    imagescan.imageList = []
    updateCounter = 0

    if searchDirectory == "":
        messagebox.showinfo(title="no path", message="no path to search")
    else:

        try:
            imagescan.scanFolders(searchDirectory)  # roep functie aan
            imagescan.imageList.sort(key=imagescan.sortFunc)
        except FileNotFoundError:
            messagebox.showinfo(title="file not found error", message=f"could not find directory: \n{searchDirectory}")

        except OSError as e:
            print(e)
            messagebox.showerror(title="OSError", message=f"error: \n{e}")

        except Exception as e:
            print(f"error: {type(e)}")
            messagebox.showerror(title="unknown error", message=f"error: \n{e}")

        display_photoNames(imagescan.imageList)

def sort_photos(event=None):
    dest = entry2.get()

    if dest == "":
        messagebox.showinfo(title="no path", message="no path to copie to")
    elif imagescan.imageList == []:
        messagebox.showinfo(title="no path", message="no pictures to sort")
    else:
        try:
            if deleteDubbels_setting.get() == True:
                imagescan.delete_byteDubbels()
                imagescan.copieTo_folders(dest)
            else:
                imagescan.copieTo_folders(dest)
        except Exception as e:
            print(f"error sort photos: {type(e)}")
            messagebox.showerror(title="unknown error", message=f"error: \n{e}")

def settingsWindow():
    global settings_window

    if settings_window is not None and settings_window.winfo_exists():
        pass
    else:
        settings_window = Toplevel()
        settings_window.title("settings")
        settings_window.geometry("200x300")
        # settings_window.iconbitmap("icon2.ico")
        checkbox = Checkbutton(settings_window, text="delete dubbels\n  (byte for byte match)  ", variable=deleteDubbels_setting)
        checkbox.grid(row=0, column=0, sticky="ew")
        checkbox2 = Checkbutton(settings_window, text ="try opening corupt files\n(may result in errors)", command=on_setting_change, variable=coruptFiles_setting)
        checkbox2.grid(row=1, column=0, sticky="ew")

def on_setting_change():
    imagescan.ImageFile.LOAD_TRUNCATED_IMAGES = coruptFiles_setting.get()
    print(imagescan.ImageFile.LOAD_TRUNCATED_IMAGES)

t1 = None

def run(function):
    global t1
    if check_t1():
        pass
        print("pass")
    else:
        t1 = Thread(target=function, daemon=True)
        t1.start()

def check_t1():
    global t1
    if t1 == None or t1.is_alive() == False:
        return False
    else:
        return True




root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=0)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_top = Frame(root)
frame_top.grid(row=0, column=0, sticky="ew")

button_settings = Button(frame_top, text="⚙️", command=settingsWindow)
button_settings.pack(side=RIGHT, fill=BOTH, expand=False)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_middle_top = Frame(root)
frame_middle_top.grid(row=1, column=0, sticky="ew")
###
# frame_middle_top.columnconfigure(0, weight=0)
# frame_middle_top.columnconfigure(1, weight=1)
# frame_middle_top.columnconfigure(2, weight=1)
# frame_middle_top.columnconfigure(3, weight=0)
# frame_middle_top.rowconfigure(0, weight=0)
###

entry = Entry(frame_middle_top)
entry.pack(side=LEFT, fill=BOTH, expand=True)
entry.bind("<Return>", search_photos)

button_1 = Button(frame_middle_top, text="select source", font=("System native", 9), command=open_searchDir)
button_1.pack(side=LEFT, expand=False)

entry2 = Entry(frame_middle_top)
entry2.pack(side=LEFT, fill=BOTH, expand=True)
entry2.bind("<Return>", sort_photos)

button_2 = Button(frame_middle_top, text="select destination", font=("System native", 9), command=open_sortDir)
button_2.pack(side=LEFT, expand=False)


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_middle = Frame(root)
frame_middle.grid(row=2, column=0, sticky="nsew")
###
frame_middle.columnconfigure(0, weight=1)
frame_middle.columnconfigure(1, weight=1)
frame_middle.rowconfigure(1, weight=1)
###

listbox = Listbox(frame_middle)
listbox.grid(row=1, column=0, sticky="nsew")
listbox.config(font=("courier", 10))

scrollBar = Scrollbar(frame_middle)
scrollBar.grid(row=1, column=1, sticky="nsw")
scrollBar.config( command = listbox.yview)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_bottom = Frame(root)
frame_bottom.grid(row=3, column=0, sticky="ew") #, columnspan=2, sticky="ew")
###
frame_bottom.columnconfigure(0, weight=1)
frame_bottom.columnconfigure(1, weight=1)
frame_bottom.columnconfigure(2, weight=1)
frame_bottom.rowconfigure(0, weight=0)
###

button_3 = Button(frame_bottom, text="search photos", font=("System native", 9), command=lambda: run(search_photos))#search_photos
button_3.grid(row=0, column=0, sticky="w")

button_4 = Button(frame_bottom, text="sort photos", font=("System native", 9), command=lambda: run(sort_photos))#sort_photos
button_4.grid(row=0, column=2, sticky="e")

# label = Label(frame_bottom, text="", font=("System native", 9))
# label.grid(row=0, column=1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

root.mainloop()