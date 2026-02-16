import os


list = os.scandir('Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten')
for entry in list :
    if entry.is_dir() or entry.is_file():
        print(entry.stat().st_ctime)
        print(entry.name)
list.close() # Sluiten is netjes om systeem resources te laten vrijmaken