def is_sql_file(fileName):
    from os.path import isfile, getsize

    if not isfile(fileName):
        return False
    if getsize(fileName) > 100:
        return False
    else:
        f = open(fileName, "rb")
        Header = f.read(100)
        f.close()
        print Header[0:20]
    log = open("fileName", "w")
    print log
if __name__ == '__main__':
    is_sql_file("newFile")