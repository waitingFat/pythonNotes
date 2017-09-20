def fun1(y):
    x = [10]
    def fun2(z):
        x[0] = x[0] +10 + y + z
        return x[0]
    return fun2

if __name__ == '__main__':
    print(fun1(5)(5))