import urllib.request
import urllib.parse
import time
import re
import os
targetPath="d:\\游戏\\MP4"
x= 0
def saveFile(path):
    # 检测当前路径的有效性
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    # 设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(targetPath, str(x)+".mp4")
    print(t)
    return t


hat = {'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 UBrowser/6.2.3831.602Safari/537.36'}
src =  urllib.request.Request(url='http://neihanshequ.com/show/',headers=hat)
src = urllib.request.urlopen(src)
data = src.read()
for i,t in set(re.findall(r'(http:[^ ]*?\.(mp4))',str(data))):
    print(i)
    try:
        x=x+1
        urllib.request.urlretrieve(i,saveFile(i))
    except Exception as a:
        print("错误",a)



