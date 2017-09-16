import urllib.request

def get_international_match_detail():
    url = "https://www.bet365.com/SportsBook.API/web?lid=10&zid=0&pd=%23AC%23B1%23C1%23D14%23E412%23F16%23S1%23&cid=99&cgid=1"
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    # request.add_header("Accept-Language", "zh-CN,zh;q=0.8")
    response = urllib.request.urlopen(request)
    with open('bet365_internationl_match_english.txt', 'w', encoding='utf-8') as f:
        f.write(response.read().decode('utf-8'))

if __name__ == '__main__':
    get_international_match_detail()