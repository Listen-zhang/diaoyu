import socket
import threading
import time
g = open("D:/游戏/b/错误.txt","w",encoding="utf-8");
class ce1(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
    # f = open("D:/游戏/b/ip1.txt","r",encoding="utf-8");
        f = ['127.0.0.1','127.0.0.1','127.0.0.1','127.0.0.1']
        for i in f:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(1)
            try:
                print(self.name)
                sk.connect((i,80))
                print(str(i)+' port 443 OK!')
                g.write(str(i) + 'is connnect')
            except Exception:
                print(str(i)+' is not connnect')
        sk.close()
a1 = ce1(1,"my_socke1",1)
a2 = ce1(2,"my_socke2",2)
a3 = ce1(3,"my_socke3",3)

a1.start()
a2.start()
a3.start()

