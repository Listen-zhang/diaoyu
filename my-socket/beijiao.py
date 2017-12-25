import socket
import threading
#创建服务套接字
ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("建立服务套接字")
#服务套接字绑定端口号，绑定主机
ss.bind(("0.0.0.0",8888))
print("绑定端口和主机")
ss.listen(5)
#接受客户套接字
print("开始等待客户的请求")
c = ss.accept()#线程阻塞
print("某个客户链接到我了")
# mag=c[0].recv(1024)
# print("mag:",mag.decode())#decode()解码,接收的数据解码
# c[0].send("是".encode())
#线程 函数
def myrevc(c):
    while True:
        msg = c.recv(1024)#当没有消息的时候休息，阻塞
        print(msg.decode())
threading._start_new_thread(myrevc,(c[0],))
while True:
    msg = input()
    c[0].send(msg.encode())