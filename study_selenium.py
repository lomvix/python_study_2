from selenium import webdriver
from selenium.webdriver import ActionChains
from urllib.parse import quote
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

brower = webdriver.Chrome()
wait = WebDriverWait(brower,10)
keyword = 'iPad'
max_page = 100

def index_page(page):
    print('第',page,'页')
    try:
        url = 'https://s.taobao.com/search?q='+quote(keyword)
        brower.get(url)
        if page>1 :
            input = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span')))
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
    except TimeoutException:
        index_page(page)

def get_products():
    html =brower.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist . items . item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
            }
        print(product)

for i in range(1,max_page+1):
    index_page(i)
    