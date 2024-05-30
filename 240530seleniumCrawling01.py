### 항상 동일 패턴 ###
from selenium import webdriver
# from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




# browser 꺼짐 방지
opt = Options()
opt.add_experimental_option('detach', True)
# browser 안보이게 하고 진행하기
#opt.add_argument('headless')

# from selenium.webdriver.support.ui import (WebDriverWait)
# from selenium.webdriver.support import expected_conditions as EC
# import sys
# import urllib.request
# import os
# from urllib.request import urlretrieve
#
# import time
# import pandas as pd
# import chromedriver_autoinstaller  # setup chrome options

url="https://www.naver.com"
drive = webdriver.Chrome(options=opt)
drive.get(url)
#time.sleep(10)
### 항상 동일 패턴 ###

# 검색창에서 키워드 입력 후 엔터
search_box = drive.find_element(By.ID,'query')
search_box.send_keys("인공지능")
search_box.send_keys(Keys.RETURN)
#time.sleep(3)
# 뉴스탭 클릭
drive.find_element(By.LINK_TEXT,'뉴스').click()  # a tag에서만 click() 사용
#time.sleep(3)
# 화면 스크롤
scroll = drive.find_element(By.TAG_NAME,'body')
for i in range(60):
    scroll.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)


# 뉴스 제목 추출
news_titles = drive.find_elements(By.CLASS_NAME,'news_tit')
# print(news_titles[0].text)
news_list = []
cn = 1
for i in news_titles:
    # print(cn, i.text)
    with open('news.csv', 'w', encoding='utf-8') as f:
        f.write(str(cn)+"."+ i.text)
        f.write('\n')
        cn+=1



drive.quit()

