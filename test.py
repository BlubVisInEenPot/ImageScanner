# moet def find_date(path): nog fixen path moet een class zijn bij: path.stat().st_...... 
# maar een pat bij: if check_fileType(path, "jpeg"):



# import gui
import os
from  datetime import *
from PIL import Image
from PIL.ExifTags import TAGS
import filetype



def getExif_data(path, data_type):
    imagename = path
    image = Image.open(imagename)
    exifdata = image.getexif()
    exif = { TAGS.get(tag_id, tag_id): value for tag_id, value in exifdata.items() }

    return(exif.get(data_type))

def find_date(entry):
    result = {}
    result_exif = {}

    try:
        result["st_atime"] = (entry.stat().st_atime)
    except:
        pass

    try:
        result["st_mtime"] = (entry.stat().st_mtime)
    except:
        pass

    try:
        result["st_ctime"] = (entry.stat().st_ctime)
    except:
        pass

    try:
        result["st_birthtime"] = (entry.stat().st_birthtime)
    except:
        pass


    if check_fileType(entry.path, "jpg"):

        if getExif_data(entry.path, "DateTime") != None:
            result_exif["Datetime"] = getExif_data(entry.path, "DateTime")

        if getExif_data(entry.path, "DateTimeOriginal") != None:
            result_exif["DateTimeOriginal"] = getExif_data(entry.path, "DateTimeOriginal")

        if getExif_data(entry.path, "DateTimeDigitized") != None:
            result_exif["DateTimeDigitized"] = getExif_data(entry.path, "DateTimeDigitized")

    for methods in result_exif:
        dt = datetime.strptime(result_exif[methods], "%Y:%m:%d %H:%M:%S")
        result[methods] = dt
    
    return result

    # return min(result.values())


def check_fileType(path, extension):
    if extension == "picture":
        imageExt = ["jpg", "png", "jpeg", "tiff", "raw", "dng", "gif", ]
    else:
        imageExt = [extension]

    i = filetype.guess(path)

    if i is None:
        return False
    else:
        for ext in imageExt:
            print(str(i.extension))
            if ext == str(i.extension):
                return True
    return False

temp_path = r"/home/OempaLoempa/Downloads/" #/home/OempaLoempa/Downloads/  #C:\Users\morten.goudswaard\Downloads #c:\Users\vboxuser\Pictures
path = os.scandir(temp_path) #gui.searchDirectory

# print(getExif_data("/home/OempaLoempa/Downloads/image.jpg", "DateTimeOriginal"))

for entry in path:
    if entry.is_file():
        print(find_date(entry))








# a = st_atime

# list = os.scandir(r"/home/OempaLoempa/Downloads")#\IMG_0332.jpg
# for entry in list:
#     if entry.is_dir() or entry.is_file():
#         print(entry.stat().a)



#print(exif.get("Make"))
#print(exif.get("DateTime"))






























# dateInSec = 0

# def get_date_taken(path):
#     # Open the image file
#     img = Image.open(path)
    
#     # Extract exif data
#     exif_data = img._getexif()
    
#     print("~~")
#     print(exif_data)
#     print("~~")

#     if not exif_data:
#         return "No EXIF data found."

#     # Search for the 'DateTimeOriginal' tag
#     for tag_id, value in exif_data.items():
#         tag_name = TAGS.get(tag_id, tag_id)
#         if tag_name == 'DateTimeOriginal':
#             return value

#     return "Date Taken tag not found."

# def get_creationDate(entry):
#     # if os.name == "nt": # windows
#     #     print("windows")
#     #     try:
#     #         return entry.stat().st_ctime
#     #     except:
#     #         return entry.stat().st_birthtime
        
#     # else:               # unix
#     #     print("unix")

#     # get_date_taken(entry)

#     print("test")

#     # try:
#     #     print("st_ctime or st_mtime")
#     #     return min(entry.stat().st_ctime, entry.stat().st_mtime)
#     # except:
#     #     print("st_birthtime")
#     #     return entry.stat().st_birthtime

# def convert_time():
#     global dateInSec

#     date = datetime.utcfromtimestamp(dateInSec)
#     return date.strftime('%d %b %Y')

# list = os.scandir(r"/home/OempaLoempa/Downloads")#\IMG_0332.jpg
# for entry in list :
#     if entry.is_dir() or entry.is_file():
#         print("_______")
#         # dateInSec = get_creationDate(entry)
#         # print(convert_time())
#         print(get_date_taken("/home/OempaLoempa/Downloads/IMG_0332.jpg"))
#         print(entry.name)
#         print("_______")
# list.close() # Sluiten is netjes om systeem resources te laten vrijmaken

# # print(get_creationDate("/home/OempaLoempa/Pictures/"))