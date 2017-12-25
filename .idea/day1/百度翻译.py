import urllib.request
import urllib.parse
import json
import re
import time
import threading
while 1==1:
    content = input('请输入需要翻译的句子：')
    data = {}
    url = 'http://fanyi.baidu.com/v2transapi'
    xh = re.compile(u'[\u4e00-\u9fa5]+')  #re模块是一个正则模块 u代表了Unicode，这两个unicode值正好是Unicode表中的汉字的头和尾。
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



    data = urllib.parse.urlencode(data).encode('utf-8')  #这个方法可以将字典转换为url参数
    request = urllib.request.Request(url=url,data=data,method='POST')
    response = urllib.request.urlopen(request)
    data1 = response.read()
    data2 = data1.decode()
    data2 =data2.replace("null","'null'")
    data2 = data2.replace("false", "'false'")
    data2 = eval(data2)
    print(data2['trans_result']['data'][0]['dst'])
#print(data2)
# print(type(data2))
# print(data2)
# print(data2['trans_result'])
#print(.decode('utf-8').encode('utf-8'))
