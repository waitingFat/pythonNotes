import urllib.parse, urllib.request

from flask import json
def getYouDao():
    while True:
        content = input("请输入内容")
        if content == ':':
            break
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc"
        data = {}
        data['i'] = "i love you"
        data['type'] = 'AUTO'
        data['doctype'] = 'json'
        data['version'] ='2.1'
        data['keyfrom'] ='fanyi.web'
        data['ue'] = 'UTF-8'
        data['typoResult'] = 'true'

        #
        # data['smartresult'] = 'dict'
        # data['client'] = 'fanyideskweb'
        # data['action'] = 'FY_BY_REALTIME'

        data = urllib.parse.urlencode(data).encode("utf-8")

        #  当需要添加header之后 必须通过构建request对象来解决问题
        req = urllib.request.Request(url, data)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        loads = json.loads(html)
        print(loads)
        print(type(loads))
        target =loads['translateResult']
        print(target[0][0]['tgt'])
        # print(loads)

def getBet365():
    url = "https://www.bet365.com/SportsBook.API/web?lid=10&zid=0&pd=%23AS%23B1%23&cid=99&cgid=1"
    header = {}
    header['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

    response = urllib.request.urlopen(url,header)
    with open("bet365FileLevel", "w") as f:
        text = response.read().decode("utf-8")
        f.write(text)

if __name__ == '__main__':
    getYouDao()
