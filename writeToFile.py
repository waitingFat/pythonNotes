import json
import urllib
import urllib2
url = "http://baidu.com"
urlopen = urllib.urlopen(url)
read = urlopen.read()
print  read
with open("webContetnFile","w") as f:
    f.write(read)
