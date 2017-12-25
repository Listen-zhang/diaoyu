import urllib.request

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
}
url="http://music.baidu.com/song/100575177"
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
data2 = response.read()
print(str(data2))