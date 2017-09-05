import os

try:
        home = os.path.expanduser("~")
        print home
        print os.name
        os.system("cls")
except Exception as e:
    print("")


