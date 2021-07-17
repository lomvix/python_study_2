import requests
from pyquery import PyQuery as pq

url='https://www.zhihu.com/explore'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
           'Host':'www.zhihu.com',
           'Cookie':'_zap=1856e5a4-d6cf-4bab-a083-97c073bfeda9; d_c0="APDUhdrqvBGPTr0dhaVWXcvQuI6BbQSMxg8=|1597515808"; _ga=GA1.2.1349653389.1597515808; _xsrf=xEnXbGWQiHLLTD0VO8t5j3w0n2Oav28W; z_c0=Mi4xT2pnbUF3QUFBQUFBOE5TRjJ1cThFUmNBQUFCaEFsVk5ZSHBIWUFCUTBZdVd0ZXpONU5qZU1zX1Ixd0pBNEhZNmNn|1599745120|dea6bb9729f3d7541da5c70e6082058e259bb0f7; q_c1=07251d1232a74d3884a01972134dd10c|1609252272000|1602410000000; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1610013488,1610028059,1610205091,1610551068; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1610551068; SESSIONID=Gjybo8hhIHPVihxnHa3VzQeIECCMUgzpKgOqGy1pg6N; JOID=VlEdB0qpXeWh-enSQqmVdacsA2Zf4zaQxpPcuyblGLT7lYSnLblfE_7x5d9Lf-L8tJTzLQsJ46yBe5h0tRfKRzE=; osd=VlASBEKpXOqi8enTTaqddaYjAG5f4jmTzpPdtCXtGLX0loynLLZcG_7w6txDf-Pzt5zzLAQK66yAdJt8tRbFRDk=; KLBRSID=2177cbf908056c6654e972f5ddc96dc2|1610551137|1610551065',
           }
response=requests.get(url,headers=headers).text
doc=pq(response)
#获取标题
items=doc('.ExploreSpecialCard.ExploreHomePage-specialCard')
for item in items.items():
    big_title=item('.ExploreSpecialCard-info').find('a').text()#大标题
    print(big_title)
    for item_2 in item('.ExploreSpecialCard-contentItem').items():
        small_title=item_2.find('a').text()#小标题
        print(small_title)
    print('\n')
