import urllib2

try:
    urllib2.urlopen("http://google.com", timeout=2)
    print ("working connection")

except urllib2.URLError:
    print ("No internet connection")


def checkUrl():
    try:
        urllib__urlopen = urllib2.urlopen("http://google.com")
        read = urllib__urlopen.read()
        print read
    except urllib2.URLError:
        print ("exception")
if __name__ == '__main__':
    checkUrl()