import os


def cal(s):
    s = s.replace(" ","")
    print s

def getLower():
    s = 'aAb'
    threeIn = """ haha,
        hehe, 
            
        xixi"""
    singleIn = "i like p'ython"
    print singleIn
    print threeIn
    print s.lower()

def mathMethod():
    methodMath = 'math.' + 'sin' + '4'
    print methodMath

def testIterator():
    print open('fileName','w')
    function = [('aaaaa',4,"a"),('vvvvvvvvv',3,'b'),('wwwwwwwww',2,'w')]
    for a, b, c in function: # interator couple
        print a
        print b
        print c
if __name__ == '__main__':
    testIterator()
