### 항상 동일 패턴 ###
import pandas as pd
from selenium import webdriver
# from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os


# browser 꺼짐 방지
opt = Options()
opt.add_experimental_option('detach', True)
# 이미지 저장 폴더 생성
save_dir = 's_images'
os.makedirs(save_dir, exist_ok=True)

drive = webdriver.Chrome(options=opt)
url="https://www.google.com"
drive.get(url)
#time.sleep(10)
### 항상 동일 패턴 ###

# 검색창에서 키워드 입력 후 엔터
keyword = "고양이 무료"
search_box = drive.find_element(By.ID,'APjFqb')
search_box.send_keys(keyword)
search_box.submit()
time.sleep(0.5)

drive.find_element(By.LINK_TEXT,'이미지').click()
time.sleep(0.5)

links=[]
images = drive.find_elements(By.CSS_SELECTOR, 'g-img.mNsIhb>img.YQ4gaf')
# print(images[0].get_attribute('src'))
# print(len(images))
for img in images:
    if img.get_attribute('src') != None:
        links.append(img.get_attribute('src'))

print('이미지 갯수:',len(links))
time.sleep(0.5)

# image download
for i, u in enumerate(links):
    urllib.request.urlretrieve(u, './'+save_dir+'/cat_'+str(i)+'.jpg')
    url_img = images[0].get_attribute('src')
# urllib.request.urlretrieve(url_img, 'test.jpg')
print('완료')
drive.quit()