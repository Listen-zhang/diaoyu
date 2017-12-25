import urllib.request

# 网址
url = "http://www.baidu.com"

# 请求
request = urllib.request.Request(url)

# 爬取结果
response = urllib.request.urlopen(request)

data = response.read()

# 设置解码方式
data = data.decode('utf-8')

# 打印结果
print(data)

# 打印爬取网页的各类信息

print(type(response))
print("-----------------------------------")
print(response.geturl())
print("-----------------------------------")
print(response.info())
print("-----------------------------------")
print(response.getcode())
