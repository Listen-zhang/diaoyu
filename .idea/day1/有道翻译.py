import urllib.request

import urllib.parse
import json
import time
import random
import hashlib

content = input('请输入需要翻译的句子：')

url = 'http://fanyi.baidu.com/sug'

data = {}
data['kw']=content

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url,data=data,method='POST')
response = urllib.request.urlopen(request)
data1 = response.read()
data2 = data1.decode()
data2 = eval(data2)
print(data2['data'])
#print(.decode('utf-8').encode('utf-8'))