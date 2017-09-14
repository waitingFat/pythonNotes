import urllib.request

import threadpool


def split():
    str = 'abc/def/g'
    split = str.split('/')
    print(split[len(split) - 1])

def test_thread_sub(item, dir):
    print(item, dir)

def  test_thread():
    items = {'a', 'b', 'c', 'd', 'e'}
    # lst_vars_1 = ['1', '2']
    # lst_vars_2 = ['4', '5']
    # func_var = [(lst_vars_1, None), (lst_vars_2, None)]
    fun_var = []
    for item in items:
        couple = []
        couple.append(item)
        couple.append('a')
        touple = (couple, None)
        fun_var.append(touple)
    pool = threadpool.ThreadPool(10)
    request = threadpool.makeRequests(test_thread_sub, fun_var)
    [pool.putRequest(req) for req in request]
    pool.wait()

def find():
    str = 'img src=http://awfafawfaw.jpg'
    find_start = str.find('img src=http')
    find_end = str.find(".jpg")
    url = str[find_start+9:find_end+4]
    print(url)

def download():
    url = "https://pic.kanlela.com/images/pic/0829250157608.jpg"
    response = urllib.request.urlopen(url)
    html=response.read()
    with open('image.jpg','wb') as f:
        f.write(html)


if __name__ == '__main__':
    link = 'abcdefg'
    link_find = link.find('a')
    print(link[link_find:link_find+2])