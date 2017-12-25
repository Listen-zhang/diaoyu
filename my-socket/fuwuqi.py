import socket
import threading
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",9999))
s.listen(5)
sock,addr =s.accept()
print("有人连接！！")
print(sock)
print(addr)
true=True
def rec(sock):
    global true
    while true:
        t=sock.recv(1024).decode('utf8')  #函数的核心语句就一条接收方法
        if t == "exit":
            true=False
        print(t)
trd=threading._start_new_thread(rec,(sock,))
while true:
    t=input()
    sock.send(t.encode('utf8'))
    if t == "exit":
        true=False
s.close()