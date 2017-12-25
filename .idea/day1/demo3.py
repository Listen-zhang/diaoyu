import urllib.request
from bs4 import BeautifulSoup

res  = urllib.request.Request("http://163.com");
res = urllib.request.urlopen(res)
soup = BeautifulSoup(res,'html.parser')
#soup = soup.select('li')
for a  in soup.select(".cm_ul_round li a"):
    h2 = a.get('href')
    print(a.text,h2)