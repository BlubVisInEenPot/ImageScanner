import os

list = os.scandir('Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten')

def calc_spaces(string,length):
    a = len(string)
    b = length - a
    return " " * b

print("SIZE                       NAME                         TYPE")
print("__________________________________________________________________________________")

for entry in list :
    if entry.is_dir() or entry.is_file():
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        if entry.is_dir():
            FileType = "Folder"
        elif entry.is_file():
            FileType = "File"

        print(str(entry.stat().st_size)[:15] + " bytes" + calc_spaces(str(entry.stat().st_size)[:15], 20) + str(entry.name)[:15] \
              + calc_spaces(str(entry.name)[:15], 30) + FileType)
        # print(entry.stat())
        # print(type(entry.stat()))

list.close() # Sluiten is netjes om systeem resources te laten vrijmaken


print(type(entry.stat()))


#print(entry.stat().st_ctime)