import requests
from lxml import etree
import random
import time

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

header = {
    'User-Agent':'{headers}',
}

def get_web_page(url):

    res = requests.get(url)
    json_loads = json.loads(res.text.lstrip('/**/HTMLPreview.loadHTML(').rstrip(');'))

    html = json_loads['query']['results']['resources']['content']
    # print(html)
    return html


def main():
   # url = 'https://www.maoyan.com/board/4'+str(offset)
    url = 'https://www.bilibili.com/anime/index/#season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1'  
   # r = get_web_page(url)
    r = requests.get(url,headers=header)
    time.sleep(3)
    html = etree.HTML(r.text)
    print(requests.get(url,headers=header).text)
    print(html)
   # text = html.xpath('//li[@class="bangumi-item"]') 
   # title=text.xpath('./li/a[@class="bangumi-title"]/text()')
    #for i in text[0:10]:
    # title=i.xpath('./tr[@class="p12"]/a/span/text()')[0].encode('ISO-8859-1').decode('gbk')
     #rank_0 = i.xpath("./i[@class='board-index board-index-1']/text()")[0]
     #title=i.xpath('./li[@class="bangumi-item"]/a[@class="bangumi-title"]/text()')[0].encode('ISO-8859-1').decode('gbk')
     #print(' ',title,'/n')

main()
