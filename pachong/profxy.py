import urllib.request

url = "http://www.whatismyip.com.tw"
proxy_support = urllib.request.ProxyHandler({'http':'177.11.17.184'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
print(response.read().decode("utf-8"))
