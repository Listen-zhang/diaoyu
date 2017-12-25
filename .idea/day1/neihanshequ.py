import urllib.request
from bs4 import BeautifulSoup

data = urllib.request.Request("https://read.qidian.com/chapter/aE5g60ksvDs1/KWQY_cZ6UnQex0RJOkJclQ2")
data = urllib.request.urlopen(data)
sop = data.read()
sop = sop.decode('utf-8')
sop = BeautifulSoup(sop,'html.parser')
out = open("D:/游戏/b/笑话.txt","w",encoding="cp936")
for a  in sop.select("p"):
    fi = a.text
    fi+="\n\n"
    print(fi)
    out.write(fi)
    print("---------------------------------")


