#!/bin/python3

import os
from defs import *

from DIC import *

def main():
    Unix("clear")
    print("Choose An Option\n\t1.Creat By Extention\n\t2.Creat By Hex")
    while True:
        OPT = int(input("-> "))
        if OPT == 1:
            autoHX()
            break
        if OPT == 2:
            myfun()
            break
        if OPT != [1, 2]:
            print("No Option Called " + str(OPT))

if __name__ == "__main__":
    main()
