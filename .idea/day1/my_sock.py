import socket
import re
import os
f = open("D:/游戏/b/ip1.txt","r",encoding="utf-8");
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.settimeout(1)
for i in f:
    try:
      print(i)
      sk.connect((i,443))
      print('Server port 80 OK!')
    except Exception:
      print('Server port 80 not connect!')
sk.close()
print("i")
# sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk.settimeout(1)
# try:
#       sk.connect(('127.0.0.1',80))
#       print('Server port 80 OK!')
# except Exception:
#       print('Server port 80 not connect!')
# sk.close()
# import random
# random.randint
