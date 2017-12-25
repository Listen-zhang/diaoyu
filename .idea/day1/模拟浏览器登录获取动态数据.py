from selenium import webdriver
from bs4 import  BeautifulSoup
from browsermobproxy import server


# serve = server.Server("C:/Users/29722/Desktop/browsermob-proxy-master/browsermob-dist/src/main/scripts/browsermob-proxy.bat")
# serve.start()
# proxy = serve.create_proxy()
# proxy.new_har("bilibili")
# content = proxy.har
# serve.stop()
# print(content)

driver =webdriver.PhantomJS(executable_path="D:/Program Files/Phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver.set_page_load_timeout(30)
# html = driver.get("http://music.baidu.com/song/100575177")
# html = driver.desired_capabilities
#js = "var url = 'http://music.163.com/ var page = require('webpage').create();page.onResourceRequested = function(request) {console.log('Request ' + JSON.stringify(request, undefined, 1));};page.onResourceReceived = function(response) {console.log('Receive ' + JSON.stringify(response, undefined, 1));};page.open(url);"
#js="var url='http://music.163.com/#/song?id=35476048';var page=require('webpage').create();page.onResourceRequested=function(request){console.log('Request '+JSON.stringify(request,undefined,1))};page.onResourceReceived=function(response){console.log('Receive '+JSON.stringify(response,undefined,1))};page.open(url);"
# js1=  driver.execute_script("<script type='text/javascript'   src='//apps.bdimg.com/cloudaapi/lightapp.js'></script> var page = require('webpage').create();")
# print(js1)
# soup = BeautifulSoup(html, 'lxml')  # 对html进行解析，如果提示lxml未安装，直接pip install lxml即可
# print(soup)
driver.close()
