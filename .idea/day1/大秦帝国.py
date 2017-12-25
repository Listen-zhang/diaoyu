
import urllib.request
import urllib.parse
import queue
import time
import timeit
from bs4 import BeautifulSoup
f = open("D:/游戏/b/小说1.txt","w",encoding="utf-8");
list = []
try:
        g = 0;
        Agent={'User-Agent':"Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML, likeGecko)Chrome/62.0.3202.89Safari/537.36"}
        res = urllib.request.Request("https://www.txtjia.com/shu/43014/",headers=Agent);
        res =  urllib.request.urlopen(res)
        soup = BeautifulSoup(res,"html.parser")
        for i in soup.select("li a "):
            ur = i.get("href")
            list.insert(g,ur)
            g+=1
            print("jing"+str(g))
except x:
  print(x)
print(list)
for i in  range(7,len(list)):
    res = urllib.request.Request("https://www.txtjia.com"+list[i]);
    print(i)
    try:
     def aa():
         global  res
         res = urllib.request.urlopen(res)
         print(res)
         soup = BeautifulSoup(res,"html.parser")
         for i in soup.select("#booktext"):
            for j in soup.select("h1"):
                biao = j.get_text()
            print(type(i))
            my_text = i.get_text()
            f.write(str(biao)+str(my_text))
    except:
      print("123")
      aa()
    try:
      aa()
    except:
      print("123")
      aa()
f.close()