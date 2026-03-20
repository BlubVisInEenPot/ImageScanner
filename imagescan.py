import os
from  datetime import *


imageList = []
DirPath = ""
sortedPath = ""
found_pictures = 0

def add_sortedFolderPath(dict_num):
    global imageList , sortedPath
    year = datetime.utcfromtimestamp(imageList[dict_num]["created"])
    print(year.strftime('%Y'))
    imageList[dict_num]["copieTo"] = sortedPath + "\\" + year.strftime('%Y')
    # geef mee dictionery nummer voeg de file location toe waar die moet staan


def delete_dubbels():
    global imageList
    if len(imageList) > 0:
        test = imageList[0]
    else:
        print("empty list")
    huidige = 1
    while huidige < len(imageList):
        if imageList[huidige]["name"] == test["name"] and imageList[huidige]["size"] == test["size"]:
            imageList.pop(huidige)
        else:
            test = imageList[huidige]
            huidige += 1

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
#  ^ vraagt voor een pat die die in DirPath zet
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
#  ^ vraagt voor een pat waar die de gesoorteerde mapjes met fotos neer zet
def sortFunc(dictionary):
    return "{:10d}".format(dictionary["size"]) + dictionary["name"].upper()  # RETURN de naam van de gegeven dictionery
#  ^ soorteert de doorgegeven dictionary eerst op naam en dan op maat
def isImage(naam): # return a True if passed extension name is in the list
    imageExt = [".jpg", ".png", ".jpeg", ".tiff", ".raw", ".dng", ".gif", ]
    for ext in imageExt:
        if ext in naam:
            return True
    return False
# ^ checkt met doorgegeven naam of een file een foto is

def scanFolders(startFolder): #
    global found_pictures, imageList
    bestandData = {} # maak lege dict aan

    list = os.scandir(startFolder) # list = start directory

    for entry in list: # ga met entry de heele lijst (directory) langs

        if entry.is_dir(): # als de entry een directory is
            scanFolders(os.path.join(startFolder, entry.name)) #zoek dan dieper

        elif entry.is_file(): # als de entry een file is
            if isImage(entry.name): # check of entry een imige is met de functie isImage()

                d = datetime.fromtimestamp(entry.stat().st_birthtime) # d = de datum ven de entry (de foto dus)
                bestandData = { "name": entry.name, "path": entry.path, "size": entry.stat().st_size, "created": entry.stat().st_birthtime } # bestandData = een dict met naam,pat,size,dateCreated er in
                imageList.append(bestandData) # voeg die dict toe aan de imageList nu is de imagelist een lijst met info over de fotos
                # print(imageList)
                # print(entry.name)
                # print(d.strftime('%d-%m-%Y'))  # 16 feb 2026
                # print("_________________________________")
                found_pictures += 1 # voeg 1 toe aan de gevonden pictures

    list.close()

#_______________________________________________________________________________________________________________________________________________

choosePath()
chooseSortedPath()

scanFolders(DirPath) # roep functie aan
print("aantal gevonden fotos: " + str(found_pictures)) # print hoe veel fotos er zijn gevenden
imageList.sort(key=sortFunc) # soorteer de image list

for i in imageList:# loop door de image list heen
    print(i["name"] + " - " + i["path"] + "  (" + str(i["size"]) + ")")# print de naam van de dictionery waar de loop is

print("_____________________")
print(imageList)
delete_dubbels()
print("_____________________")

add_sortedFolderPath(2)

print(imageList)
# copieTo_folders(2)
