"""
argument is to explain terminal language
 includes four steps
"""
import argparse


def testArgumentParse():
    #step1
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    #step2
    parser.add_argument('work_dir',metavar='WORK_DIR',type=str,nargs=1)
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    args = vars(parser)

    def main():
        """
        """
    print "main invoke"
if __name__ == "__main__":
        testArgumentParse()