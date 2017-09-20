"""
    step1 打开start 网页  解析下载规律
    step2 寻找想要的标签 find 截取url
    step3 将截取的url 拼接成下载地址 保存到文件

"""

import urllib.request
import threadpool

# 打开网页操作
import os
from time import time


def open_url(url):
    request = urllib.request.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    response = urllib.request.urlopen(request)
    return response.read()


def find_page_num():
    url = "http://se.haoa06.com/listhtml/2.html"
    html = open_url(url)
    html = html.decode("utf-8")
    page_start = html.find('a href=')
    page_end = html.find(']', page_start, page_start + 30)
    # print(page_end)
    # print(html[page_start+23])
    page_num = html[page_start + 23:page_end]
    return page_num


def download_all_imag(url):
    prefixx_url = "http://se.haoa05.com"
    print(url)
    request = urllib.request.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    response = urllib.request.urlopen(url)
    html = response.read()
    decode_html = html.decode("utf-8")
    image_list = []
    start_query = 0
    while True:
        if decode_html.find('img src=', start_query) != -1:
            start_imag_url = decode_html.find('img src=')  # +9
            imag_url_end = decode_html.find('.jpg', start_imag_url, start_imag_url + 255)
            imag_url = html[start_imag_url + 9:imag_url_end + 4]
            print(imag_url)
            image_list.append(imag_url)
            start_query += 9
        else:
            return image_list


def get_every_page_img():
    #  http://jandan.net/ooxx/page-100#comments
    page_num = int(find_page_num())
    print(page_num)
    for a in range(page_num - 1):
        url = 'http://jandan.net/ooxx/page-' + str(a + 1) + '#comments'
        page_num -= 1
        imag = download_all_imag(url)
        print(imag.__sizeof__())
    pass


def download_every_page(page_num):
    url = "http://se.haoa06.com/listhtml/2-" + str(page_num) + ".html"
    print(url)
    response = open_url(url)
    html = response.decode('utf-8')
    detail_list_imag = find_detail_page(html)
    get_every_page_detail(detail_list_imag, str(page_num))

def get_first_page_img():
    page_count = 287
    # pool = threadpool.ThreadPool(25)
    # requests = threadpool.makeRequests(download_single_detail_imags, couples)
    # [pool.putRequest(req) for req in requests]
    # pool.wait()
    page_list = []
    for page in range(page_count):
        page_list.append(page)
    pool = threadpool.ThreadPool(25)
    requests = threadpool.makeRequests(download_every_page, page_list)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    # page_num = page +2
    # url = "http://se.haoa05.com/listhtml/2-" + str(page_num) + ".html"
    # response = open_url(url)
    # html = response.decode('utf-8')
    # detail_list_imag = find_detail_page(html)
    # get_every_page_detail(detail_list_imag, str(page_num))


def find_detail_page(html):
    detail_page_list = []
    start_position = 0
    while True:
        detail_position = html.find('a href="/html', start_position)
        start_position = detail_position
        print(detail_position)
        if detail_position != -1:
            detail_position_end = html.find('target', detail_position + 10, detail_position + 50)
            detail_page_list.append(html[detail_position + 8:detail_position_end - 2])
            start_position += 10
        else:
            return detail_page_list


# http://se.haoa05.com/html/115318.html
# http://se.haoa05.com
def download_single_detail_imags(root_dir, page):
    # root_dir = "C:\\Users\\zym\\Desktop\\images"
    url_prefixx = "http://se.haoa06.com"
    detail_url = url_prefixx + page
    response = open_url(detail_url)
    html = response.decode('utf-8')
    split = page.split('/')
    directory = root_dir + "/" + split[len(split) - 1]  # 子目录
    os.makedirs(directory)
    os.chdir(directory)
    start_position = 0
    while True:
        find = html.find('img src="http', start_position)
        start_position = find
        if find != -1:
            image_right = html.find('.jpg', start_position)
            image_url = html[start_position + 9:image_right + 4]
            start_position += 10
            print(image_url)
            response = open_url(image_url)
            split = image_url.split('/')
            file_name = directory + "/" + split[len(split) - 1]
            with open(file_name, 'wb') as f:
                f.write(response)
        else:
            return


def write_file(file_name):
    with open(file_name, 'w') as f:
        f.write("a")


def get_every_page_detail(detail_list_imag, page_num):
    root_dir = "C:\\Users\\zym\\Desktop\\images\\" + str(page_num)
    couples = []
    print('------len-------', len(detail_list_imag))
    for detail_item in detail_list_imag:
        couple_item = []
        couple_item.append(root_dir)
        couple_item.append(detail_item)
        touple = (couple_item, None)
        couples.append(touple)
    os.makedirs(root_dir)
    os.chdir(root_dir)
    pool = threadpool.ThreadPool(25)
    requests = threadpool.makeRequests(download_single_detail_imags, couples)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    # for page in detail_list_imag:
    #     download_single_detail_imags(page, root_dir)


if __name__ == '__main__':
    # html = open_url()
    # html = html.decode("utf-8")
    # with open("source.txt", "w", encoding='utf-8') as f:
    #     f.write(html)
    #  create_ima_dir("C:\\Users\\zym\\Desktop\\images")
    # get_every_page_img()
    html = get_first_page_img()
