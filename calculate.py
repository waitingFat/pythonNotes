import sys

import os


def __test__():
    major = sys.version_info.major
    print major
    while True:
        k = raw_input("\ninput a number")# read from console as a str nomatter whatever you input
        # k = input("\ninput a number") # it has a type concept
        if k.__eq__('100'):
            break

def __testArgs__():
    print sys.argv
    print sys.argv[0]
    os.system(sys.argv[1])

def __testArraySub__():
    array = ['a','b','c','d','e']
    b = array[:3]
    print ('#'*80)
    print b

def openFile(fileName):
    with open(fileName,"r") as f:
        read = f.read()
        print read
