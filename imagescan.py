import os
import shutil
import tkinter as tk
from  datetime import *

# to do
# 1: in bytedubbel en dubbel functie delete de gene die het niewste is
# 2:


imageList = []
DirPath = ""
sortedPath = ""

def makedir(i): # make the directories
    try:
        os.makedirs(i)
    except FileExistsError:
        pass
    except PermissionError:
        print("permision denied")
    except Exception as e:
        print(f"An error occurred: {e}")
    #os.path.exists(i):

def add_sortedFolderPath(): # add the sorted folder locations to the dictionarys
    global imageList , sortedPath
    for file in range(0, len(imageList)):
        date = datetime.utcfromtimestamp(imageList[file]["created"])
        imageList[file]["destFolder"] = os.path.join(sortedPath, date.strftime('%Y'), date.strftime('%B'))

def copieTo_folders(): # copie all photos to the sorted folder locations
    global imageList

    for dict in imageList:
        makedir(dict["destFolder"])
        shutil.copy2(dict["path"], dict["destFolder"])

def delete_byteDubbels():
    global imageList

    buffersize = 1048576
    counter = 0

    if not len(imageList) > 0:
        print("empty list")

    while counter + 1 < len(imageList):

        filePath1 = imageList[counter]["path"]
        filePath2 = imageList[counter + 1]["path"]

        try:
            print(f'byte comparing {filePath1}')
            with open(filePath1, "rb") as file1:
                print(f'and {filePath2}')
                with open(filePath2, "rb") as file2:
                    while True:
                        bytes1 = file1.read(buffersize)
                        bytes2 = file2.read(buffersize)

                        if bytes1 != bytes2:
                            counter += 1
                            break

                        elif not bytes1:
                            imageList.pop(counter)
                            break
        except  Exception as e:
            print('File error: ', e)

def delete_dubbels():
    global imageList

    if len(imageList) > 0: # als de lengte van imageList groter is dan 0
        vorige = imageList[0] # maak een variable aan vorige = het eerste ding in imageList
    else:
        print("empty list") # print anders empty list
    huidige = 1 # maak een variable aan huidig is 1
    while huidige < len(imageList): # als huidig(1) klijner is dan de lengte van imagelist loop
        if imageList[huidige]["name"] == vorige["name"] and imageList[huidige]["size"] == vorige["size"]: # als de naam van de huidige gelijk is als de naam van de vorige en de size
            imageList.pop(huidige) #
        else:
            vorige = imageList[huidige]
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
    looping = True

    while looping:
        chosenPath = input("path to store sorted folders (blank = default): ")

        if chosenPath == "":
            sortedPath = "Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten\sorted photos"
            break
        elif os.path.exists(chosenPath):
            sortedPath = chosenPath
            break
        elif not os.path.exists(chosenPath):
            print("path does not exist")
            correctInput = False
            while correctInput == False:
                i = input("do you want to make it y/n: ")
                if i == "y":
                    correctInput = True
                    makedir(chosenPath)
                    sortedPath = chosenPath
                    looping = False # needs to break out of both loops
                elif i == "n":
                    correctInput = True
                elif i != "y" or i != "n":
                    print("type y for yes or n for no")

        else:
            print("error")
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
    global imageList
    bestandData = {} # maak lege dict aan

    list = os.scandir(startFolder) # list = start directory

    for entry in list: # ga met entry de heele lijst (directory) langs

        if entry.is_dir(): # als de entry een directory is
            scanFolders(os.path.join(startFolder, entry.name)) #zoek dan dieper

        elif entry.is_file(): # als de entry een file is
            if isImage(entry.name): # check of entry een imige is met de functie isImage()

                bestandData = { "name": entry.name, "path": entry.path, "size": entry.stat().st_size, "created": entry.stat().st_birthtime } # bestandData = een dict met naam,pat,size,dateCreated er in
                imageList.append(bestandData) # voeg die dict toe aan de imageList nu is de imagelist een lijst met info over de fotos

    add_sortedFolderPath()
    list.close()

def cli():
    choosePath()
    chooseSortedPath()
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    scanFolders(DirPath)  # roep functie aan
    imageList.sort(key=sortFunc)  # soorteer de image list
    allPictures = len(imageList)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    while True:
        userInput = input("delete dubbel images by (size and name)(1) or (byte by byte)(2): ")
        if userInput == "1":
            delete_dubbels()  # delete the pictures with the same name and size
            break
        elif userInput == "2":
            delete_byteDubbels()
            break
        else:
            print("choose an option by typing the corresponding number. eg 2")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    copieTo_folders()  # copie the fount pictures to thare sorted folder path
    print(str(allPictures) + " images found| " + str(allPictures - len(imageList)) + " images deleted| " + str(len(imageList)) + " images sorted|")
#_______________________________________________________________________________________________________________________________________________

cli()