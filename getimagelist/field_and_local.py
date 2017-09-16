num = 10
def modify():
    global num
    num = 8
    print(num)

if __name__ == '__main__':
    print(num)
    modify()
    print(num)