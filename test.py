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


    if check_fileType(entry.path, ["jpg", "tiff", "jpeg", "heic", "heif", "hif", "heics", "heifs", "avci"]):

        if getExif_data(entry.path, "DateTime") != None:
            result_exif["Datetime"] = getExif_data(entry.path, "DateTime")

        if getExif_data(entry.path, "DateTimeOriginal") != None:
            result_exif["DateTimeOriginal"] = getExif_data(entry.path, "DateTimeOriginal")

        if getExif_data(entry.path, "DateTimeDigitized") != None:
            result_exif["DateTimeDigitized"] = getExif_data(entry.path, "DateTimeDigitized")

    for methods in result_exif:
        dt = datetime.strptime(result_exif[methods], "%Y:%m:%d %H:%M:%S")
        result[methods] = dt
    
    print(min(result, key = result.get))
    return min(result.values())


def check_fileType(path, extension):
    if extension == "picture":
        imageExt = ["jpg", "png", "jpeg", "tiff", "raw", "dng", "gif", "heic", "heif", "hif", "heics", "heifs", "avci"]
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
