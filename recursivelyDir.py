import os
from stat import S_ISDIR, S_ISREG
import sys


def dirTree(top, callback):
        if not os.path.exists(top):
            print "---isexist-----"
            return
        else:
            listdir = os.listdir(top)
            for f in listdir:
                mode = os.stat(os.path.join(top, f)).st_mode
                print mode
                if S_ISDIR(mode):
                    print f, " is a directory"
                    dirTree(os.path.join(top, f))
                elif S_ISREG(mode):
                    callback(f)
                    print f, "is a file"
def callback(f):
    print f, "----callback---"

if __name__ == '__main__':
    print sys.argv[1]
    dirTree(sys.argv[1], callback(file))