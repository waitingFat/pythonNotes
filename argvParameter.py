from sys import argv

# script, input_file = argv # getFileName from argv
import os

print argv

# currentFile = open(input_file)
def print_all(fileName):
    print fileName.read()


def print_line(lineCount, f):
    print lineCount, f.readline()


def seek_To_Start(fileName):
    fileName.seek(0)


# print "file let's print all file"
# print_all(currentFile)
# lineCount = 1
# print "let's print first line  before this you must execute seek(0) at first"
# print "so let's execute seek(0)"
# seek_To_Start(currentFile)
# print_line(lineCount,currentFile)  # if we do not execute seek(0) it will print nothing
# currentFile.close()

if __name__ == '__main__':
    funtion = ["aa", "bb", 'cc']
    fileName = argv[1]
    print fileName
    currentFile = open(fileName)  # receive an string parameter and return a file
    file_Start = os.stat(fileName)
    print file_Start
    a, b, c = funtion
    # print  a, b, c
    intValue = 16
    intValue >>= 1
    # print intValue
