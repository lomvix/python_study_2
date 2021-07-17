import requests
import random
import urllib
import re
from lxml import etree

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]

proxy_list = [

]


def get_content(headers):

	randdom_header=random.choice(headers)
	return randdom_header

headers = get_content(my_headers)
#proxy = {'https':get_content(proxy_list)}

header = {
    'User-Agent':'{headers}',
    'Cookie':'_zap=1856e5a4-d6cf-4bab-a083-97c073bfeda9; d_c0="APDUhdrqvBGPTr0dhaVWXcvQuI6BbQSMxg8=|1597515808"; _ga=GA1.2.1349653389.1597515808; _xsrf=xEnXbGWQiHLLTD0VO8t5j3w0n2Oav28W; z_c0=Mi4xT2pnbUF3QUFBQUFBOE5TRjJ1cThFUmNBQUFCaEFsVk5ZSHBIWUFCUTBZdVd0ZXpONU5qZU1zX1Ixd0pBNEhZNmNn|1599745120|dea6bb9729f3d7541da5c70e6082058e259bb0f7; q_c1=07251d1232a74d3884a01972134dd10c|1609252272000|1602410000000; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1610013488,1610028059,1610205091,1610551068; SESSIONID=j7Im7qzJqBCZTFpd3GrmpQR9EqMVOV8kSsSr9kWCNtJ; JOID=VFoXA0I2Xc9kJ8pSJzCWV23wJuUyWGqEAB-_KG9IG4w8eoMmQxeGOz0szlAs_G51UkNXv5zh51pgag321nAsGrM=; osd=U1oSBkwxXcphKc1SIjWYUG31I-s1WG-BDhi_LWpGHIw5f40hQxKDNTosy1Ui-25wV01Qv5nk6V1gbwj40XApH70=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1610617285; KLBRSID=ca494ee5d16b14b649673c122ff27291|1610618627|1610616908'
}


url = 'https://www.zhihu.com/hot'
f=open('zhihu.txt','w')
def get_question_num(url,headers):
    response = requests.get(url, headers=header)
    text = response.text
    html = etree.HTML(text)
    reslut = html.xpath("//section[@class='HotItem']")
    question_list = []
    for question in reslut[0:50]:
        number = question.xpath("./div[@class='HotItem-index']//text()")[0].strip()
        title = question.xpath(".//h2[@class='HotItem-title']/text()")[0].strip()
        href = question.xpath("./div[@class='HotItemx-content']/a/@href")[0].strip()
        question_num = href.split('/')[-1]
        question_list.append([question_num, title])
        print(number,'\n',title,'\n',href)
        f.write(number+'\n'+title+'\n'+href+'\n')
    return question_list

question=str(get_question_num(url,headers))
#with open('zhihu.txt','w') as f:
#  f.writelines(question)
#r=requests.get(url,headers=header)
#h = '<h2><a href="//zhuanlan.zhihu.com/p/343708950" target="_blank" rel="noopener noreferrer" data-za-detail-view-element_name="Title" data-za-detail-view-id="2812">Google 和苹果，为什么都想让你安装新系统</a>'
#pattern = re.compile('<a.*?href.*?target>(.*?)</a>',re.S)
#title = re.search('<h2.*?href.*?target>(.*?)</a>',h,re.S)
#print(title.group(1))
#rearch = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',h,re.S)
#print(rearch.group(1),rearch.group(2))
#print(r.text)