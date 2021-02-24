# Functions Will Creat in this File

import os

def Unix(CMD):
    print('> ' + CMD)
    os.system(CMD)


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
