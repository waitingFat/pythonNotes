import urllib2
url = "http://www.bet365.com/?&cb=105802117941#/AC/B1/C1/D8/E66907337/F3/S1/P^14/Q^938/"
urlopen = urllib2.urlopen(url)
with open('newFileName', 'w') as f:
    f.write(urlopen.read())
