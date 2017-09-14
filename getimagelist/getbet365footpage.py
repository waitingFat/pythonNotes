import urllib.request
def  get_bet_html(url):
    request = urllib.request.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

def find_tag(url):
    html = get_bet_html(url)
    html_encoded = html.decode('utf-8')
    with open('bet_page', 'w', encoding='utf-8') as f:
        f.write(html_encoded)

if __name__ == '__main__':
    url = "https://www.bet365.com/#/AS/B1/"
    find_tag(url)