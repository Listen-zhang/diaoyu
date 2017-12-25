import urllib.request
import urllib.parse
import urllib.response
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import threading
def hhhh():
    try:
        i = 0;
        while True:
            i+=1
            p = ""
            w = ""
            gg = 0
            while True:
                gg += 1
                w += chr(random.randint(97, 122))
                p += str(random.randint(0, 9))
                if gg == 10:
                    break
            print("账号:" + p)
            print("密码:" + w)
            url = 'http://www.yufan100.com.cn/logo.pdf'
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = (
        #"Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043128 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D PA QQ/7.0.0.3135 NetType/4G WebP/0.3.0 Pixel/1080"
         "Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 QQ/6.7.1.416 V1_IPH_SQ_6.7.1_1_APP_A Pixel/750 Core/UIWebView NetType/4G QBWebViewType/1"
            )
            service_args = [
                '--proxy=222.246.23.117:8888',  # 代理 IP：prot    （eg：192.168.0.28:808）
                '--proxy-type=http'            # 代理类型：http/https
            ]

            driver =webdriver.PhantomJS(executable_path="D:/Program Files/Phantomjs-2.1.1-windows/bin/phantomjs.exe",desired_capabilities=dcap)
            driver.set_script_timeout(10)
            driver.set_page_load_timeout(10)
            html = driver.get(url)
            uid = driver.find_element_by_id('u')
            uid.send_keys(p)
            pwd = driver.find_element_by_id('p')
            pwd.send_keys(w)
            driver.find_element_by_id('go').click()
            driver.refresh()
            driver.close()
            driver.quit()
            # print('搜索后的页面源码：\n', driver.page_source)  # 页面源码
            print(i)
            if i ==100:
                break
    except  Exception as a:
        print("错误",a)
        driver.quit()
        ee()
def ee():
    t2 = threading.Thread(target=hhhh)
    while True:
            if 3 > threading.active_count():
                t2.start()
                break
ee()
# driver = webdriver.PhantomJS(executable_path='./phantomjs', desired_capabilities=dcap)
# url = 'http://www.budanwang.cn/?Url=http://url.cn/56mzRDn?Dosq'
# t = {'User-Agent':'Mozilla/5.0 (Linux; Android 5.1; OPPO R9tm Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043128 Safari/537.36 V1_AND_SQ_7.0.0_676_YYB_D PA QQ/7.0.0.3135 NetType/4G WebP/0.3.0 Pixel/1080'}
# res = urllib.request.Request(url,headers=t)
# res = urllib.request.urlopen(res)
# soup = BeautifulSoup(res, 'html.parser')
# print(soup)