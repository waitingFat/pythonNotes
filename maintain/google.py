#encoding = gbk
"""
Author: Ankit Agarwal (ankit167)
Usage: python google.py <keyword>
Description: Script googles the keyword and opens
             top 5 (max) search results in separate
             tabs in the browser
Version: 1.0
"""

import webbrowser, sys, pyperclip, requests, bs4


def main():
    if len(sys.argv) > 1:
        keyword = ' '.join(sys.argv[1:])
    else:
        # if no keyword is entered, the script would search for the keyword
        # copied in the clipboard
        keyword = pyperclip.paste()

    res = requests.get('http://google.com/search?q=' + keyword)

    with open("movie_details", "w") as f:
        f.write(res.text)

    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    link_Elems = soup.select('.r a') #寻找class = r 里的a标签
    numOpen = min(2, len(link_Elems))

    for i in range(numOpen):
        webbrowser.open('http://google.com' + link_Elems[i].get('href'))

if __name__ == '__main__':
    main()
