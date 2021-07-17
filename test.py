import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

url = 'http://www.weather.com.cn/textFC/hb.shtml'
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

response = requests.get(url, headers=header)
response = response.text.encode("raw_unicode_escape").decode("utf-8")
soup = BeautifulSoup(response,"html5lib") 
div = soup.find("div",class_="conMidtab")
tables = div.find_all("table")
print(response.text)