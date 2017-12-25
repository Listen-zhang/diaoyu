# !/usr/bin/env python3
# coding=utf-8
# XX 网站模拟登录
import sys  # for sys.argv
import urllib
import urllib.request
import urllib.parse

url = 'http://xxx'


def login():
    action = 'login'
    username = 'xxx'  # 可将密码等保存至文件
    password = 'xxx'
    ac_id = 6
    type = 1
    data = {'action': action,
            'username': username,
            'password': password,
            'ac_id': ac_id,
            'type': type
            }
    postdata = urllib.parse.urlencode(data).encode('utf-8')
    try:
        request = urllib.request.Request(url, postdata)
        response = urllib.request.urlopen(request)
        # 从结果内容中查找是否有特定字符串
        if (response.read().decode('utf-8').find('login_ok') > 0):
            print('login_ok')
    except Exception as e:
        print('oops!Please check network!')
        print(e)


def logout():
    logoutdata = {'action': 'logout'}
    postdata = urllib.parse.urlencode(logoutdata).encode('utf-8')
    request = urllib.request.Request(url, postdata)
    response = urllib.request.urlopen(request)
    print(response.read().decode('utf-8'))  # 根据情况解码


if __name__ == '__main__':
    if len(sys.argv) == 1:
        login()
    else:  # 如果有额外参数,则退出登录
        logout()