import os
from  datetime import *

# ik was bij de 7de page van pdf

def isImage(naam):
    imageExt = [".jpg", ".png", ".jpeg", ".tiff", ".raw", ".dng", ".gif", ]
    for ext in imageExt:
        if ext in naam:
            return True
    return False

def scanFolders(startFolder):
    global found_pictures

    # print("Inhoud van" + startFolder)
    list = os.scandir(startFolder)

    for entry in list:

        if entry.is_dir():
            # print('[' + entry.name + ']')
            scanFolders(os.path.join(startFolder, entry.name))

        elif entry.is_file():
            if isImage(entry.name):
                d = datetime.fromtimestamp(entry.stat().st_birthtime)

                print(entry.name)
                print(d.strftime('%d-%m-%Y'))  # 16 feb 2026
                print("_________________________________")
                found_pictures += 1

    list.close()

found_pictures = 0

scanFolders('Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten')
print("aantal gevonden fotos: " + str(found_pictures))


list = os.scandir('Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten')


























# def calc_spaces(string,length):
#     a = len(string)
#     b = length - a
#     return " " * b
#
# print("SIZE                       NAME                         TYPE"                    "DATE")
# print("______________________________________________________________________________________________")
#
# for entry in list :
#     if entry.is_dir() or entry.is_file():
#         print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
#
#         if entry.is_dir():
#             FileType = "Folder"
#         elif entry.is_file():
#             FileType = "File"
#
#         print(str(entry.stat().st_size)[:15] + " bytes" + calc_spaces(str(entry.stat().st_size)[:15], 20) + str(entry.name)[:15] \
#               + calc_spaces(str(entry.name)[:15], 30) + FileType)
#         # print(entry.stat())
#         # print(type(entry.stat()))
#
# list.close() # Sluiten is netjes om systeem resources te laten vrijmaken
#
#
# print(type(entry.stat()))
#
#
# #print(entry.stat().st_ctime)