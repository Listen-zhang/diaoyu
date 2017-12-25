import urllib.request
import re
import requests

# def login():
#     session = requests.Session()
#     # res = session.get('http://my.its.csu.edu.cn/').content
#
#     login_data = {
#         'username':'Curiosity',
#         'password':'zxjzxj',
#         'verifycode':'2329',
#         'CookieDate':'0',
#         'imageField.x':'40',
#         'imageField.y':'11',
#          "Accept-Encoding": "gzip, deflate",
#     }
#     session.post('http://free.3v.do/member/chk_login.as', data=login_data)
#     print("123")
#     res = session.get(url='http://free.3v.do/member/index.asp')
#     #print(res.text)
# login()
import requests


def login():
    session = requests.session()
    # res = session.get('http://my.its.csu.edu.cn/').content
    login_data = {
        'id':'7',
        'pwd':'123'
    }
    session.post('http://localhost:8080/liao/', data=login_data)
    res = session.get('http://localhost:8080/liao/a/b')
    print(res.text)


login()