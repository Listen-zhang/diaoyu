import threading
import time
import random
class Thread1(threading.Thread):
    def run(self):
        for i in range(1,11):
            if i==3:  #当Thread1运行到3的时候进入
                cond.acquire() #锁
                cond.wait()  #等待Thread2运行完成
                cond.release()
            print(i)
            time.sleep(1)


class Thread2(threading.Thread):
    def run(self):
        for i in range(30,19,-1):
            print(i)
            time.sleep(1)
        cond.acquire()
        cond.notify()  #唤醒
        cond.release()

lock = threading.Lock()
cond = threading.Condition(lock=lock)
t1 = Thread1()
t2 = Thread2()
t1.start()
t2.start()