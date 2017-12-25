import urllib.request
import urllib.parse
from  selenium import webdriver #模拟浏览器访问
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import os

##检查路径
def saveFile(path,url=None):
    # 检测当前路径的有效性
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
    except Exception as t:
        return t
    # 设置每个图片的路径
    if url==None:
        pass
    else:
        pos = str(url).rindex('/')
        t = os.path.join(path, url[pos + 1:])
        return t
## 下载
def xiazhai(data,urll):
    for g in data :
        try:
            print(g)
            urllib.request.urlretrieve(g[0],saveFile(urll,url=g[0]),)
        except Exception as ff:
            print("错误", ff)


url = input("请输入搜索的位置:")
caidan="esc:退出\n"
driver =webdriver.PhantomJS(executable_path="D:/Program Files/Phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.set_page_load_timeout(10)
html = driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
# ii = url.index(":")
tupian =  set(re.findall(r'(http[^ ]*?\.(bmjp|pg|png|tiff|gif|pcx|tga|exif|fpx|svg|psd|cdr|pcd|dxf|ufo|eps|ai|raw|WMF))',str(soup)))
print("图片完成")
video  =  set(re.findall(r'(http[^ ]*?\.(mp4|avi|mov|wmv|mpg))',str(soup)))
print("视频完成")
text   =  set(re.findall(r'(http[^ ]*?\.(txt|docx))',str(soup)))
print("文本完成")
audio  =  set(re.findall(r'(http[^ ]*?\.(mp3|wma)\?[^\s]*)',str(soup)))
print("音频完成")
def hqu():
    if len(tupian)!=0:
        print("123")
        global caidan
        caidan = caidan+"1.下载图片：图片数量"+ str(len(tupian))
    if len(video)!=0:
        caidan = caidan+"2.下载视频：视频数量" + str(len(video))
    if len(text)!=0:
        caidan = caidan+"3.下载文本：文本数量" + str(len(text))
    if len(audio)!=0:
        caidan = caidan+"4.下载音频：音频数量" + str(len(audio))
hqu()
xuanzei  = input(caidan)
if(xuanzei!="esc"):
    path = input("请输入下载路径：")
    print(saveFile(path))
else:
    pass
if int(xuanzei) == 1:
    xiazhai(tupian,path)
if int(xuanzei) == 2:
    xiazhai(video, path)
if int(xuanzei) == 3:
    xiazhai(text, path)
if int(xuanzei) == 4:
    xiazhai(audio, path)
hqu()

# print(tupian)
# print(video)
# print(text)
# print(audio)






