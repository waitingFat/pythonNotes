#encoding=gbk
"""
    step1 打开start 网页  解析下载规律
    step2 寻找想要的标签 find 截取url
    step3 将截取的url 拼接成下载地址 保存到文件

"""

import urllib.request
import threadpool

# 打开网页操作
import os

def open_url(url):
    request = urllib.request.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    response = urllib.request.urlopen(request)
    return response.read()

# 下载每页视频
def download_every_page(page_num):
    #http://www.ja321.net/xflist/57_3.html
    url = "http://www.ja321.net/xflist/57_" + str(page_num) + ".html"
    response = open_url(url)
    html = response.decode('utf-8')
    down_load_video(html)

# start thread works with page
def prepare_page():
    page_count = 1
    page_list = []
    for page in range(page_count):
        page_list.append(page+2)
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(download_every_page, page_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()

def down_load_video(html):
    root_dir = "C:\\Users\\zym\\Desktop\\video\\"
    os.makedirs(root_dir)
    os.chdir(root_dir)
    url_prefixx = "http://www.ja321.net"
    start_position = 0
    while True:
        link_start = html.find('href=', start_position)
        start_position = link_start + 1
        print(html[link_start+6:link_start+12])
        if((link_start != -1) & (html[link_start:link_start+6] == "/xfvod")):
            link_end = html.find('"', link_start+8)
            url = html[link_start + 6:link_end-1]
            print(link_start, link_end)
            print(url_prefixx, url)
        else:
            if((link_start != -1)):
                continue
            else:
                return
def find_detail_page(html):
    url_start = html.find('a class="play-img" href=')
    if url_start != -1:
        url_end = html.find('.html',url_start)
        url = html[url_start+25, url_end +5]
        print(url)
        down_load_video(url)

if __name__ == '__main__':
    prepare_page()