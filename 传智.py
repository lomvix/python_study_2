import requests
from lxml import etree

url="http://stu.ityxb.com/lookPaper/busywork/08951a862e6843db85191ccb3200cff7"

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

print(requests.get(url,headers=header).text)