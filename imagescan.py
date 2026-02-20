import os
from  datetime import *

# list = os.scandir('Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten')
#
#
# for entry in list:
#     d = datetime.fromtimestamp(entry.stat().st_birthtime)
#
#     print(d.strftime('%d-%m-%Y')) # 16 feb 2026

def scanFolders(startFolder):
    print("Inhoud van" + startFolder)
    list = os.scandir(startFolder)
    for entry in list:
        if entry.is_dir():

            print('[' + entry.name + ']')
            scanFolders(os.path.join(startFolder, entry.name))
        elif entry.is_file():
            print(entry.name)
    list.close()

scanFolders('Y:\Digibende\Amstelveen\Kandidaten\Programmeren\morten')

# print(d)



























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