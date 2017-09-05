"""
  os is the block of python main useful is to operator file dir no matter what the operator system is
"""
import os


def FindPwdInWindows():
    print os.name
    print os.getcwd()
    print os.path.abspath()
    os.makedirs("a/b")
if __name__ == "__main__":
    FindPwdInWindows()