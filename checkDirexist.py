from __future__ import print_function

import sys

import os

def main():
    if sys.version_info.major >= 3:
        input_method = input
    else:
        input_method = input

    CheckDir = input_method("Enter the name of the directory to check:")
    print()

    if os.path.exists(CheckDir):
        print ("the file exist")
    else:
        print ("no directory found for" + CheckDir)
        print()
        os.makedirs(CheckDir)
        print ("create directory for" + CheckDir)

if __name__ == '__main__':
    main()