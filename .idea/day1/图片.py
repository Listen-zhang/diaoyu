#coding = utf-8
import urllib.request
import re
from bs4 import BeautifulSoup

def html1(html):
    url =urllib.request.Request(html)
    res =urllib.request.urlopen(url)
    get_img=res.read()
    get_img = get_img.decode('utf-8')
#     print(get_img)
#     urllib.request.urlretrieve(get_img, '%s.png' % "123")
# html1("http://www.huawei.com/cn/?utm_source=bdpz&utm_campaign=regular&utm_medium=cpc")
    return get_img
def da(html2):
    imgre = re.compile(r'<img src="" class="img-responsive center-block lazy" alt="" data-original="(http://www-file.huawei.com/.+)"')
    imglist = re.findall(imgre,repr(html2))
    print(imglist)
    x=0
    for imgurl in  range(0,len(imglist)):
        data3 = html1(imglist[10])
        num = 0
        with open('%s.png'%num,'wb')as fp:
            fp.write(data3)
            num=num+1
            print(num)
        # urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        # x=x+1
html='http://www.huawei.com/cn/?utm_source=bdpz&utm_campaign=regular&utm_medium=cpc'
data2 = html1(html)
da(data2)








# def getHtml(url):
#     page = urllib.request.urlopen(url)
#     html = page.read()
#     return html
#
# def getImg(html):
#     reg = 'src="(.+?\.jpg)" alt='
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, html)
#     x = 0
#     for imgurl in imglist:
#         urllib.request(imgurl, '%s.jpg' % x)
#         x+=1
#     return imglist
#
# html = getHtml("http://pic.yxdown.com/list/0_0_1.html")
#
# getImg(html)