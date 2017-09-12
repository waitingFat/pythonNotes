#encoding=utf-8
import urllib.request
# response = urllib.request.urlopen("http://placekitten.com/g/200/200")

request = urllib.request.Request("http://placekitten.com/g/200/200")
response = urllib.request.urlopen(request)
# html = response.read()
# print(html)
# html = html.decode("utf-8")  # 将输出格式化
with open("b.jpg", "wb") as f:  #wb 写入二进制文件数据
    f.write(response.read())
# print(response.read().decode("utf-8"))
# info = response.info()
# print(info)
