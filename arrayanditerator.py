import os


def __testArray__():
    global isYes
    isYes = False
    global array
    array = ['a', 'b', 'c', 'd', 'e']
    array_list = list(array)
    array_list.remove('a')
    print array_list.__len__()
    for s in array:
        if s.__eq__('cC'):
            print 'yes'
            isYes = True
            break
    if not isYes:
        print 'no'

if __name__ == '__main__':
    print os.path.isfile("newFile")
    with open('newFile', 'a') as f:
        if os.access('newFile', os.R_OK):
            f.write("------a")
            f.close()
