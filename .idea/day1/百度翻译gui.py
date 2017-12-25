from tkinter import *
import socket
import threading
import time
import urllib.request
import urllib.parse
import json
import re
root = Tk()
root.title(('百度翻译'))
true=True
def rec(s):
        content = s.decode("utf8")
        print(content)
        data = {}
        url = 'http://fanyi.baidu.com/v2transapi'
        xh = re.compile(u'[\u4e00-\u9fa5]+')  # re模块是一个正则模块 u代表了Unicode，这两个unicode值正好是Unicode表中的汉字的头和尾。
        # "[]"代表里边的值出现一个就可以，后边的“+”代表至少出现1次，合起来即至少匹配一个汉字。
        match = xh.search(content)
        if match:
            data['query'] = content
            data['from'] = 'zh'
            data['transtype'] = 'translang'
            data['simple_means_flag'] = 3
            data['to'] = 'en'
        else:
            data['query'] = content
            data['from'] = 'en'
            data['transtype'] = 'translang'
            data['simple_means_flag'] = 3
            data['to'] = 'zh'
        data = urllib.parse.urlencode(data).encode('utf-8')  # 这个方法可以将字典转换为url参数
        request = urllib.request.Request(url=url, data=data, method='POST')
        response = urllib.request.urlopen(request)
        data1 = response.read()
        data2 = data1.decode()
        data2 = data2.replace("null", "'null'")
        data2 = data2.replace("false", "'false'")
        data2 = eval(data2)
        yi = data2['trans_result']['data'][0]['dst']
        text_msglist.insert(END, content+":", 'green')
        text_msglist.insert(END, yi+"\n")

#线程
# trd=threading._start_new_thread(rec,(s,))
#发送按钮事件
def sendmessage():
  #在聊天内容上方加一行 显示发送人及发送时间

  rec(str(text_msg.get()).encode('utf8'))
  text_msg.delete(0,END)

frame_left_top   = Frame(width=380, height=270, bg='white')
frame_left_center  = Frame(width=380, height=30,borderwidth = 3)
frame_left_bottom  = Frame(width=40, height=30)
##创建需要的几个元素
text_msglist    = Text(frame_left_top)
text_msg      = Entry(frame_left_center);
button_sendmsg   = Button(frame_left_bottom, text='翻译', command=sendmessage)

#创建一个绿色的tag
text_msglist.tag_config('green', foreground='#008B00')
#使用grid设置各个容器位置
frame_left_top.grid(row=2, column=0)
frame_left_center.grid(row=1, column=0, padx=0, pady=0)
frame_left_bottom.grid(row=1, column=1)
frame_left_top.grid_propagate(0)
frame_left_center.grid_propagate(0)
frame_left_bottom.grid_propagate(0)
#把元素填充进frame
text_msglist.grid()
text_msg.grid()
button_sendmsg.grid(sticky=E)
#主事件
root.mainloop()