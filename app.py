#!/bin/python3

import os
from defs import *

def main():
    Unix("clear")
    print("Choose An Option\n\t1.Creat By Extention\n\t2.Creat By Hex")
    while True:
        OPT = int(input("-> "))
        if OPT == 1:
            break
        if OPT == 2:
            myfun()
            break
        if OPT != [1, 2]:
            print("No Option Called " + str(OPT))

main()
