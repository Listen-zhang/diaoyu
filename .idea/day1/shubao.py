
import urllib.request
import queue
import time
import timeit
import re
import threading
import random
from bs4 import BeautifulSoup
i =1 ;
f = open("D:/游戏/b/小说.txt","w",encoding="cp936");
f.close()
hat = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"}
res=None
poi = [{"http":"114.249.113.219:9000"},{"http":"114.255.212.17:808"},{"http":"112.74.94.142:3128"}]
def xiazhai(data,urll):
    for g in set(re.findall(r'(http://down1.bookbao8.com:8026/fulltext/[^ ]*?\.(txt))', str(data))):
        try:
            urllib.request.urlretrieve(g[0], urll,)
        except Exception as ff:
            print("错误", ff)
while True:
    # print(random.choice(poi))
    # httppi=urllib.request.ProxyHandler(random.choice(poi))
    # opener = urllib.request.build_opener(httppi, urllib.request.HTTPHandler)
    # urllib.request.install_opener(opener)
    # 代理ip
    if(i==1):
      i=i+1;
      res =urllib.request.Request("https://www.bookbao8.com/bookList-c_6-t_0-o_1.html",headers=hat);
    else:
      res =urllib.request.Request("https://www.bookbao8.com/bookList-p_"+str(i)+"-c_6-t_0-o_1.html",headers=hat);
      i = i + 1;
      print(i)
    res = urllib.request.urlopen(res)
    print("123")
    soup = BeautifulSoup(res,'html.parser')
    #soup = soup.select('li')
    for a  in soup.select(".bookname a"):
        h2 = a.get('href')
        h2 = str(h2).strip("/book")
        dizhi = "https://www.bookbao8.com/down/"+h2
        text = str(a.text)
        text = text.replace("/",",")
        text = text.replace("?", ",")
        urll = "D:/游戏/小说/"+text+".txt"
        res = urllib.request.Request(dizhi, headers=hat);
        res = urllib.request.urlopen(res)
        data = res.read()
        t2 = threading.Thread(target=xiazhai,args=(data,urll,))
        if 3>threading.active_count():
            t2.start()
        else:
            while True:
                if 3>threading.active_count():
                    t2.start()
                    break

       # urllib.request.urlretrieve(dizhi,urll)
