from sys import argv

import os

from os.path import getsize

try:
    directory = argv[1]
except IndexError:
    print "must provide an argument"

dirSize = 0
for (path, dirs, files) in os.walk(directory):  #first binary top level files and dirs then the sub
    l = list(files)
    print "---------", l.__sizeof__()
    for file in files:
        fileName = os.path.join(path, file)
        dirSize += getsize(fileName)
    print path
    print file
    print dirs
print dirSize