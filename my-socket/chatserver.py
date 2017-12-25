'''
设计多人聊天转发消息的服务
要有两个线程
一个在收消息
一个在把收到的消息发出去
'''
import  socket
import threading
ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.bind(("0.0.0.0",9999))
ss.listen(10)
msg=None
lock=threading.Lock()
con=threading.Condition(lock)
zu = ["",""]
def server_recv(c,a):
    global msg
    while True:
        msg1=c.recv(3000)
        con.acquire()
        msg=msg1
        zu[0] = str(a)
        zu[1] = msg1.decode()
        msg=str(zu)
        con.notify_all()
        con.release()

def server_send(c,a):
    global msg
    while True:
        con.acquire()
        con.wait()
        con.release()
        c.send(msg.encode())
# i = 0 ;
# zidain = {}
# #获取所有连接客户没有实现
# def faip(c,a):
#      con.acquire()
#      i=+1;
#      zidain.setdefault(a,i)
#      print(str(zidain))
#      #c.send(str(zidain).encode("utf8"))
#      con.notify_all()
#      con.release()
while True:
    c,a=ss.accept()
    #threading._start_new_thread(faip,(c,a))
    threading._start_new_thread(server_recv,(c,a))
    threading._start_new_thread(server_send,(c,a))