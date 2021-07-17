from selenium import webdriver

url = 'http://jx.618g.com/?url=https://www.iqiyi.com/v_19rrjd6d20.html'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
videoAnalysis = browser.get(url)
videoName = browser.title   
print(videoName)
videoSrcAll = browser.find_element_by_id('player').get_attribute('src')
print(videoSrcAll)
browser.close()
#提取一次m3u8
getShortSrc = res.split('\n')[2]   
print(getShortSrc)
noindexurl = url.replace('index.m3u8', '')   
trueUrl = noindexurl + getShortSrc   
print(trueUrl)
# 提取二次m3u8
res1 = requests.get(trueUrl).text
print(res1)
#m3u8请求

