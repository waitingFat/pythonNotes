import urllib.request

url = "http://www.baidu.com"
def openWeb1():
    response = urllib.request.urlopen(url)
    print(response.getcode())
    print(response.read())

def openWeb2():
    request = urllib.request.Request(url)
    request.add_header("user-agent","Mozilla/5.0")
    response = urllib.request.urlopen(request)
    print(response.getcode)
    print(response.read())

if __name__ == '__main__':
    openWeb2()