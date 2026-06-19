from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, messagebox, Tk, ttk
import imagescan
from threading import Thread


root = Tk()

root.geometry("600x300")
root.minsize(550, 200)
root.title("image sorter")

icon = PhotoImage(file="icon.png")
icon2 = PhotoImage(file="icon2.png")
root.iconphoto(False, icon)


# searchDirectory = r"C:\Users\morten.goudswaard\Downloads"

deleteDubbels_setting = BooleanVar()
deleteDubbels_setting.set(True)
coruptFiles_setting = BooleanVar()
coruptFiles_setting.set(False)
sortByMonth = BooleanVar()
sortByMonth.set(True)

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
    #delete items in treeview
    treeview.delete(*treeview.get_children())
    for item in treeview.get_children():
        treeview.delete(item)
    #add items from list in treeview(name, date)
    for index, item in enumerate(list):
        treeview.insert("", END, text=index, values=(item["name"], item["destFolder"]))
    
previous_value = 0
def update_folder_label(count):
    global previous_value

    if not count == "done":
        previous_value = count

    if count == "done":
        root.after_idle(lambda: label.config(text=f"scanned folders: {previous_value} done"))
    else:
        root.after_idle(lambda: label.config(text=f"scanned folders: {count} running..."))

def update_sorting_label(is_running):
    # If is_running is True, show "Sorting...", otherwise show "done" (or clear it)
    if is_running == "clear":
        status_text = ""
    elif is_running == True:
        status_text = "Sorting..." 
    else:
        status_text = "done"
    
    root.after_idle(lambda: label_2.config(text=status_text))

def search_photos(event=None):
    global searchDirectory
    searchDirectory = entry.get()
    imagescan.imageList = []

    update_sorting_label("clear")
    imagescan.dirs_scanned = 0
    update_folder_label(0)
    #get all selected filetypes
    extList = []
    for var in vars_dict:
        if vars_dict[var].get():
            extList.append(var)
    print(f"sortByMonth setting: {sortByMonth.get()}")

    if searchDirectory == "":
        messagebox.showinfo(title="no path", message="no path to search")
    else:

        try:
            imagescan.scanFolders(searchDirectory,  extList, sortByMonth.get(), callback=update_folder_label)  # roep functie aan
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

    update_folder_label("done")

def sort_photos(event=None):
    dest = entry2.get()

    if dest == "":
        messagebox.showinfo(title="no path", message="no path to copie to")
    elif imagescan.imageList == []:
        messagebox.showinfo(title="no path", message="no pictures to sort")
    else:
        try:
            update_sorting_label(True)

            if deleteDubbels_setting.get() == True:
                imagescan.delete_byteDubbels()

            imagescan.copieTo_folders(dest, callback=update_sorting_label)
        except Exception as e:
            print(f"error sort photos: {type(e)}")
            messagebox.showerror(title="unknown error", message=f"error: \n{e}")
            update_sorting_label(False)

    print()
    if imagescan.check_log():
        messagebox.showinfo(title="errors", message=f"{imagescan.error_amount} errors acured\nmore info in errors.txt")

#create variables for menu buttons
extLabels = ["jpg", "png", "jpeg", "tiff", "raw", "dng", "gif", "heic", "heif", "hif", "heics", "heifs", "avci"]
vars_dict = {ext: IntVar(value=1) for ext in extLabels}
def settingsWindow():
    global settings_window, icon2, extLabels, vars_dict

    if settings_window is not None and settings_window.winfo_exists():
        pass
    else:
        settings_window = Toplevel()
        settings_window.title("settings")
        settings_window.geometry("200x300")
        settings_window.iconphoto(False, icon2)
        # wigets
        # checkboxes
        checkbox = ttk.Checkbutton(settings_window, text="delete dubbels\n  (byte for byte match)  ", variable=deleteDubbels_setting)
        checkbox.grid(row=0, column=0, sticky="ew")
        checkbox2 = ttk.Checkbutton(settings_window, text ="try opening corupt files\n(may result in errors)", command=on_setting_change, variable=coruptFiles_setting)
        checkbox2.grid(row=1, column=0, sticky="ew")
        checkbox3 = ttk.Checkbutton(settings_window, text="also sort by month",variable=sortByMonth)
        checkbox3.grid(row=2, column=0, sticky="ew")
        # menu button with checkboxes for file types
        menubutton = ttk.Menubutton(settings_window, text="filetypes")
        #craate menu attached to menu button
        menubutton.menu = Menu(menubutton, tearoff=0)
        menubutton["menu"] = menubutton.menu

        #add checkbuttons to the menu
        for ext, var_obj in vars_dict.items():
            menubutton.menu.add_checkbutton(label=ext, variable=var_obj)
        #put in grid
        menubutton.grid(row=3, column=0, sticky="w")

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


buttonIcon = icon2.subsample(2, 2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=0)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=0)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_top = ttk.Frame(root)
frame_top.grid(row=0, column=0, sticky="ew")

button_settings = ttk.Button(frame_top, image = buttonIcon, command=settingsWindow)
button_settings.pack(side=RIGHT, fill=BOTH, expand=False)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_middle_top = ttk.Frame(root)
frame_middle_top.grid(row=1, column=0, sticky="ew")

entry = ttk.Entry(frame_middle_top)
entry.pack(side=LEFT, fill=BOTH, expand=True)
entry.bind("<Return>", search_photos)

button_1 = ttk.Button(frame_middle_top, text="select source", command=open_searchDir)
button_1.pack(side=LEFT, expand=False)

entry2 = ttk.Entry(frame_middle_top)
entry2.pack(side=LEFT, fill=BOTH, expand=True)
entry2.bind("<Return>", sort_photos)

button_2 = ttk.Button(frame_middle_top, text="select destination", command=open_sortDir)
button_2.pack(side=LEFT, expand=False)


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_middle = ttk.Frame(root)
frame_middle.grid(row=2, column=0, sticky="nsew")

treeview = ttk.Treeview(frame_middle, columns=("test", "test2"))

treeview.column("#0", width=70, stretch=False)
treeview.column("#1", width=380)
treeview.column("#2", width=130, stretch=False)

treeview.heading("#0", text="num")
treeview.heading("#1", text="name")
treeview.heading("#2", text="date")

scrollbar = ttk.Scrollbar(frame_middle, orient=VERTICAL, command=treeview.yview)
treeview.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, expand=False, fill=BOTH)
treeview.pack(side=RIGHT, expand=True, fill=BOTH)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
frame_bottom = ttk.Frame(root)
frame_bottom.grid(row=3, column=0, sticky="ew") #, columnspan=2, sticky="ew")
###
frame_bottom.columnconfigure(0, weight=1)
frame_bottom.columnconfigure(1, weight=1)
frame_bottom.columnconfigure(2, weight=1)
frame_bottom.columnconfigure(3, weight=1)
frame_bottom.rowconfigure(0, weight=0)
###

button_3 = ttk.Button(frame_bottom, text="search photos", command=lambda: run(search_photos))
button_3.grid(row=0, column=0, sticky="w")

button_4 = ttk.Button(frame_bottom, text="sort photos", command=lambda: run(sort_photos))
button_4.grid(row=0, column=3, sticky="e")

label = ttk.Label(frame_bottom, text="scanned folders: 0")
label.grid(row=0, column=1)

label_2 = ttk.Label(frame_bottom, text="")
label_2.grid(row=0, column=2)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

root.mainloop()