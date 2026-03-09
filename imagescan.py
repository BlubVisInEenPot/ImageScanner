import os
from  datetime import *


imageList = []
DirPath = ""
sortedPath = ""
found_pictures = 0

def choosePath():
    global DirPath

    while True:
        chosenPath = input("path to search (blank = default): ")

        if chosenPath == "":
            DirPath = "Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten"
            break
        elif os.path.exists(chosenPath):
            DirPath = chosenPath
            break
        else:
            print("path does not exist")

def chooseSortedPath():
    global sortedPath

    while True:
        chosenPath = input("path to store sorted folders (blank = default): ")

        if chosenPath == "":
            sortedPath = "Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten\sorted photos"
            break
        elif os.path.exists(chosenPath):
            sortedPath = chosenPath
            break
        else:
            print("path does not exist")

def sortFunc(dictionary):
    return "{:10d}".format(dictionary["size"]) + dictionary["name"].upper()  # RETURN de naam van de gegeven dictionery

def isImage(naam): # return a True if passed extension name is in the list
    imageExt = [".jpg", ".png", ".jpeg", ".tiff", ".raw", ".dng", ".gif", ]
    for ext in imageExt:
        if ext in naam:
            return True
    return False


def scanFolders(startFolder):
    global found_pictures, imageList
    bestandData = {}

    list = os.scandir(startFolder)

    for entry in list:

        if entry.is_dir():
            scanFolders(os.path.join(startFolder, entry.name))

        elif entry.is_file():
            if isImage(entry.name):

                d = datetime.fromtimestamp(entry.stat().st_birthtime)
                bestandData = { "name": entry.name, "path": entry.path, "size": entry.stat().st_size, "created": entry.stat().st_birthtime }
                imageList.append(bestandData)
                # print(imageList)
                # print(entry.name)
                # print(d.strftime('%d-%m-%Y'))  # 16 feb 2026
                # print("_________________________________")
                found_pictures += 1

    list.close()


choosePath()


scanFolders(DirPath) # roep functie aan
print("aantal gevonden fotos: " + str(found_pictures)) # print hoe veel fotos er zijn gevenden
imageList.sort(key=sortFunc) # soorteer de image list

for i in imageList:# loop door de image list heen
    print(i["name"] + " - " + i["path"] + "  (" + str(i["size"]) + ")")# print de naam van de dictionery waar de loop is























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