# Functions Will Creat in this File

import os
from DIC import *
# NOTE: Simple base
def Unix(CMD):
    print('> ' + CMD)
    os.system(CMD)
def File_Gen(SZ, NM, etn):
    Unix("truncate -s " + SZ + "M " + NM)
    print("File Created")
    Unix("xxd -r -p -o 0 <(echo " + etn + ") "  + NM)
    print("File Ready In " + NM)

# NOTE: Advanced main
def myfun():
    print("File Size In MB(Only number)?")
    Size = input("Size: ")
    print("File Name? ")
    NAME = input("Filename: ")
    PATH = "output/" + NAME
    Unix("truncate -s " + Size + "M " + PATH)
    print("FIle Created\nBut It's ASCI file to change it to valid file\n enter Your hex signature\n without any spaces and others")
    HEX = input("HEX: ")
    Unix("xxd -r -p -o 0 <(echo " + HEX + ") " + PATH)
    print("Your File Is Ready(To Use) in the " + PATH)

def autoHX():
    FS = input("Size(MB): ")
    Fn = input("Name: ")
    PATH = "output/" + Fn
    print("File Extention\n\t1.mp3\n\t2.pdf\n\t3.ZIP\n\t4.PNG\n\t5.Ogg\n\t6.Rar")
    while True:
        INP = int(input("INP: "))
        if INP == 1:
            EXT = MP3
            File_Gen(FS, PATH, EXT)
            break
        if INP ==  2:
            EXT = PDF
            File_Gen(FS, PATH, EXT)
            break
        if INP == 3:
            EXT = ZIP
            File_Gen(FS, PATH, EXT)
            break
        if INP == 4:
            EXT = PNG
            File_Gen(FS, PATH, EXT)
            break
        if INP == 5:
            EXT = OGG
            File_Gen(FS, PATH, EXT)
            break
        if INP == 6:
            EXT = RAR
            File_Gen(FS, PATH, EXT)
            break
        if INP in [1, 2, 3, 4, 5, 6]:
            pass
        else:
            print("Nothing Called " + str(INP))
