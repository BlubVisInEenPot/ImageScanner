import os
from  datetime import *

dateInSec = 0

def get_creationDate(entry):
    # if os.name == "nt": # windows
    #     print("windows")
    #     try:
    #         return entry.stat().st_ctime
    #     except:
    #         return entry.stat().st_birthtime
        
    # else:               # unix
    #     print("unix")
    try:
        print("st_ctime or st_mtime")
        return min(entry.stat().st_ctime, entry.stat().st_mtime)
    except:
        print("st_birthtime")
        return entry.stat().st_birthtime

def convert_time():
    global dateInSec

    date = datetime.utcfromtimestamp(dateInSec)
    return date.strftime('%d %b %Y')

list = os.scandir("/home/OempaLoempa/Downloads")
for entry in list :
    if entry.is_dir() or entry.is_file():
        print("_______")
        dateInSec = get_creationDate(entry)
        print(convert_time())
        print(entry.name)
        print("_______")
list.close() # Sluiten is netjes om systeem resources te laten vrijmaken

# print(get_creationDate("/home/OempaLoempa/Pictures/"))