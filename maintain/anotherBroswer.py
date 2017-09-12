# encoding='gbk'
import sys
import webbrowser

import bs4
import pyperclip  # 哈哈
import requests


def main():
    if len(sys.argv) > 1:
        keywords = ''.join(sys.argv[1:])  # 当前粘贴版内容
    else:
        keywords = pyperclip.paste()

    res = requests.get('https://www.bet365.com')
    # print(res.raise_for_status())
    soup = bs4.BeautifulSoup(res.text, "html.parser")  # parse the html
    soup_find_all = soup.find_all(href='https://www.bet365.com/zh-CHS/')

    res = requests.get('https://www.bet365.com/zh-CHS/')
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    with open('../newFileName2', 'w', encoding='utf-8')as f:
        f.write(str(soup.text))
    # print(soup.title)
    find_all = soup.findAll()
    # for tag in find_all:
        # print(tag)

    linkElems = soup.select('.r a')
    # print(linkElems)
    numOpen = min(2, len(linkElems))
    # print(numOpen)

    for i in range(numOpen):
        webbrowser.open("http://google.com" + linkElems[i].get('href'))


if __name__ == '__main__':
    main()
