import os

def get_creationDate(entry):
    if os.name == "nt":
        print("windows")
        return entry.stat().st_birthtime
        
    else:
        print("unix")
        return entry.stat().st_ctime

    

list = os.scandir("C:\Program Files")#"/home/OempaLoempa/Pictures/"
for entry in list :
    if entry.is_dir() or entry.is_file():
        print(get_creationDate(entry))
        # print(type(entry))
list.close() # Sluiten is netjes om systeem resources te laten vrijmaken

# print(get_creationDate("/home/OempaLoempa/Pictures/"))