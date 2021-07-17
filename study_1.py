from selenium import webdriver
from lxml import etree

brower = webdriver.Chrome()

url = 'https://www.bilibili.com/anime/index/#season_version=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=1'  
brower.get(url)
text = brower.find_elements_by_xpath('//li[@class="bangumi-item"]')
for i in text[0:50]:
    print(i.text)
#print(brower.page_source)
brower.close()
