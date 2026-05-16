import os

if os.name == "posix":
    print("unix")

elif os.name == "nt":
    print("windows")
    
else:
    print("?")

# list = os.scandir("/home/OempaLoempa/Pictures/")
# for entry in list :
#     if entry.is_dir() or entry.is_file():
#         print(entry.stat().st_ctime)
#         print(entry.name)
# list.close() # Sluiten is netjes om systeem resources te laten vrijmaken