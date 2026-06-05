import os
import shutil
import tkinter as tk
from PIL import ImageTk, Image, ImageFile
from PIL.ExifTags import TAGS
from pillow_heif import register_heif_opener
from  datetime import *
import filetype

register_heif_opener()
ImageFile.LOAD_TRUNCATED_IMAGES = False

imageList = []
searchDir = ""
sortDir = ""

error_amount = 0

def clear_log():
    with open("errors.txt", "wt") as f:
        f.write("")

def log_errors(exeption):
    global error_amount

    error_amount += 1
    with open("errors.txt", "at") as f:
        f.write(f"- {exeption}\n\n")

def check_log():
    with open("errors.txt", "rt") as f:
        if f.read() == "":
            return False
        else:
            return True

def makedir(i): # make the directories
    try:
        os.makedirs(i)
    except FileExistsError:
        pass
    except PermissionError:
        log_errors(f"makedir(): prmision denied")

    except Exception as e:
        log_errors(f"makedir(): {e}")


def add_sortedFolderPath(): # add the sorted folder locations to the dictionarys
    global imageList , sortDir
    for file in range(0, len(imageList)):
        date = imageList[file]["created"]
        imageList[file]["destFolder"] = os.path.join(date.strftime('%Y'), date.strftime('%B'))


def copieTo_folders(dest, callback=None): # copie all photos to the sorted folder locations
    global imageList, running

    for dict in imageList:
        destination = os.path.join(dest, dict["destFolder"])
        makedir(destination)
        shutil.copy2(dict["path"], destination)

    
    if callback:
        callback(False)

def delete_byteDubbels():
    global imageList

    buffersize = 1048576
    counter = 0

    if not len(imageList) > 0:
        # print("no imeges in list (def delete_byteDubbels)")
        pass
    while counter + 1 < len(imageList):

        filePath1 = imageList[counter]["path"]
        filePath2 = imageList[counter + 1]["path"]

        try:
            with open(filePath1, "rb") as file1:
                with open(filePath2, "rb") as file2:
                    while True:
                        bytes1 = file1.read(buffersize)
                        bytes2 = file2.read(buffersize)

                        if bytes1 != bytes2:
                            counter += 1
                            break

                        elif not bytes1:
                            imageList.pop(counter)
                            break
        except  Exception as e:
            log_errors(f"delete_byteDubbels(): {e}")

# def delete_dubbels():
#     global imageList
#
#     if len(imageList) > 0: # als de lengte van imageList groter is dan 0
#         vorige = imageList[0] # maak een variable aan vorige = het eerste ding in imageList
#     else:
#         print("empty list") # print anders empty list
#     huidige = 1 # maak een variable aan huidig is 1
#     while huidige < len(imageList): # als huidig(1) klijner is dan de lengte van imagelist loop
#         if imageList[huidige]["name"] == vorige["name"] and imageList[huidige]["size"] == vorige["size"]: # als de naam van de huidige gelijk is als de naam van de vorige en de size
#             imageList.pop(huidige) #
#         else:
#             vorige = imageList[huidige]
#             huidige += 1

def sortFunc(dictionary):
    return "{:10d}".format(dictionary["size"]) + dictionary["name"].upper()  # RETURN de naam van de gegeven dictionery
#  ^ soorteert de doorgegeven dictionary eerst op naam en dan op maat
def check_fileType(path, extension):
    if extension == "picture":
        imageExt = ["jpg", "png", "jpeg", "tiff", "raw", "dng", "gif", "heic", "heif", "hif", "heics", "heifs", "avci"]
    else:
        imageExt = extension

    i = filetype.guess(path)

    if i is None:
        return False
    else:
        for ext in imageExt:
            if ext == str(i.extension):
                return True
    return False

def getExif_data(path, data_type):
    try:
        imagename = path
        image = Image.open(imagename)
        exifdata = image.getexif()
        exif = { TAGS.get(tag_id, tag_id): value for tag_id, value in exifdata.items() }
        return(exif.get(data_type))
    
    except OSError as e:
        log_errors(f"getExif_data(): {e}\nwith file: {path}")

def find_date(entry):
    result = {}
    result_exif = {}

    try:
        result["st_atime"] = datetime.utcfromtimestamp(entry.stat().st_atime)
    except:
        pass

    try:
        result["st_mtime"] = datetime.utcfromtimestamp(entry.stat().st_mtime)
    except:
        pass

    try:
        result["st_ctime"] = datetime.utcfromtimestamp(entry.stat().st_ctime)
    except:
        pass

    try:
        result["st_birthtime"] = datetime.utcfromtimestamp(entry.stat().st_birthtime)
    except:
        pass


    if check_fileType(entry.path, ["jpg", "tiff", "jpeg", "heic", "heif", "hif", "heics", "heifs", "avci"]):#["jpg", "tiff", "jpeg", "heic", "heif", "hif", "heics", "heifs", "avci"]
        if getExif_data(entry.path, "DateTime") != None: #and getExif_data(entry.path, "DateTime") != "0000:00:00 00:00:00":
            result_exif["Datetime"] = getExif_data(entry.path, "DateTime")

        if getExif_data(entry.path, "DateTimeOriginal") != None: #and getExif_data(entry.path, "DateTimeOriginal") != "0000:00:00 00:00:00":
            result_exif["DateTimeOriginal"] = getExif_data(entry.path, "DateTimeOriginal")

        if getExif_data(entry.path, "DateTimeDigitized") != None: #and getExif_data(entry.path, "DateTimeDigitized") != "0000:00:00 00:00:00":
            result_exif["DateTimeDigitized"] = getExif_data(entry.path, "DateTimeDigitized")

    try:
        for methods in result_exif:
            dt = datetime.strptime(result_exif[methods], "%Y:%m:%d %H:%M:%S")
            result[methods] = dt
    except:
        pass
    
    return min(result.values())

dirs_scanned = 0
def scanFolders(startFolder, callback=None): #
    global imageList, dirs_scanned
    bestandData = {} # maak lege dict aan

    try:
        list = os.scandir(startFolder) # list = start directory
        for entry in list: # ga met entry de heele lijst (directory) langs

            if entry.is_symlink():
                pass

            elif entry.is_dir(): # als de entry een directory is
                dirs_scanned += 1

                if callback:
                    callback(dirs_scanned)

                if not(entry.name.startswith("$")):
                    scanFolders(os.path.join(startFolder, entry.name), callback=callback) #zoek dan dieper
                else:
                    log_errors(f"scanFolders(): cannot scan system folder {entry.name}")
                

            elif entry.is_file(): # als de entry een file is
                if check_fileType(entry.path, "picture"):

                    bestandData = { "name": entry.name, "path": entry.path, "size": entry.stat().st_size, "created": find_date(entry)} # bestandData = een dict met naam,pat,size,dateCreated er in
                    imageList.append(bestandData) # voeg die dict toe aan de imageList nu is de imagelist een lijst met info over de fotos

        add_sortedFolderPath()
        list.close()

    except PermissionError:
        log_errors(f"scanFolders(): permission error")
        pass

clear_log()