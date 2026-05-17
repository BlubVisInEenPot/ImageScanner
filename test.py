import os
from  datetime import *
from PIL import Image
from PIL.ExifTags import TAGS




def getExif_data(path, data_type):
    imagename = path
    image = Image.open(imagename)
    exifdata = image.getexif()
    exif = { TAGS.get(tag_id, tag_id): value for tag_id, value in exifdata.items() }

    return(exif.get(data_type))

def find_date(path):
    result = {}

    try:
        result["st_atime"] = (path.stat().st_atime)
    except:
        result["st_atime"] = 0

    try:
        result["st_mtime"] = (path.stat().st_mtime)
    except:
        result["st_mtime"] = 0

    try:
        result["st_ctime"] = (path.stat().st_ctime)
    except:
        result["st_ctime"] = 0    

    try:
        result["st_birthtime"] = (path.stat().st_birthtime)
    except:
        result["st_birthtime"] = 0
    




    return min(result.values())

    
list = os.scandir(r"/home/OempaLoempa/Downloads")

for entry in list:
    print(entry.stat().st_type)



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