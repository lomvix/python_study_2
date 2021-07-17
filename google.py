import requests
from lxml import etree

url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"

header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

f=open('google.txt','w')

def main():

  html=etree.HTML(requests.get(url,headers=header).text)
  text = html.xpath('//div[@class="xrnccd F6Welf R7GTQ keNKEd j7vNaf"]') 
  for i in text[0:45]:
       title=i.xpath("./a[@class='list-title']/text()")[0].encode('ISO-8859-1').decode('gbk')
       href = i.xpath("./a[@class='list-title']/@href")[0]
       print(title,'\n',href,'\n')
       f.write(title+'\n'+href+'\n')

main()
