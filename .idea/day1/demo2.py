from bs4 import BeautifulSoup
import  urllib.request,re
url="http://localhost:8080/login";
re = urllib.request.Request(url);
re = urllib.request.urlopen(re);
#re.read();
#soup = BeautifulSoup(re)
date  = BeautifulSoup(re,'html.parser')
#date  = date.select("img")
print(date);
