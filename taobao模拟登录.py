from selenium import webdriver
from selenium.webdriver import ActionChains
from urllib.parse import quote
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq

brower = webdriver.Chrome()
url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9DVnegE&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
brower.get(url)
