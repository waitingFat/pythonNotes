def ListToCouple():
    listFirst = ["zhangsan", "lisi", "wangwu"]
    listSecond = ["23", "43", "19"]
    print list(zip(listFirst, listSecond))

if __name__ == '__main__':
    ListToCouple()