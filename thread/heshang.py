import threading
import time
import random
# class Mythread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         print("Mythread")
#     def run(self):
#         for i in range(1,11):
#             print(i)
#             time.sleep(1)
#     def start(self):
#         print("开始Mythread")
#         super().start()
# t=Mythread()
# t2 = Mythread()
# t.start()
# t2.start()
# lock = threading.Lock()
# cond = threading.Condition(lock=lock)
# class Thread1(threading.Thread):
#     def run(self):
#         for i in range(1,11):
#             if i==3:
#                 cond.acquire()
#                 cond.wait()  #等待
#                 cond.release()
#             print(i)
#             time.sleep(1)
#
#
# class Thread2(threading.Thread):
#     def run(self):
#         for i in range(30,19,-1):
#             print(i)
#             time.sleep(1)
#         cond.acquire()
#         cond.notify()
#         cond.release()
#
# lock = threading.Lock()
# cond = threading.Condition(lock=lock)
# t1 = Thread1()
# t2 = Thread2()
# t1.start()
# t2.start()
class Huofu(threading.Thread):
    def __init__(self,name=None):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        while True:
            cond.acquire()
            if len(guo)==0:
                for i in range(1,11):
                    guo.append(i)
                    print('做出第{0}个馒头'.format(i))
                    time.sleep(1)
                cond.notify_all()
                cond.release()
            cond2.acquire()
            cond2.wait()
            cond2.release()

class Chihuo(threading.Thread):
    def __init__(self,name=None):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        while True:
            mantou=None
            cond.acquire()
            if len(guo)==0:
                cond2.acquire()
                cond2.notify()
                cond2.release()
                cond.wait()
            else:
                mantou=guo.pop()
            cond.release()
            if mantou is not None:
                print('{0}正在吃{1}'.format(self.name,mantou))
                time.sleep(random.randint(1,5))

guo = []
lock = threading.Lock()
cond = threading.Condition(lock=lock)#吃的锁
lock2 = threading.Lock()
cond2 = threading.Condition(lock=lock2)#蒸馒头的锁
Huofu(name='做饭和尚').start()
Chihuo(name='长眉和尚吃饭').start()
Chihuo(name='短眉和尚吃饭').start()
Chihuo(name='中眉和尚吃饭').start()