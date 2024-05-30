### 항상 동일 패턴 ###
import pandas as pd
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

# 검색어 입력
singer = input('가수입력')

drive = webdriver.Chrome(options=opt)
url="https://www.melon.com/index.htm"
drive.get(url)
#time.sleep(10)
### 항상 동일 패턴 ###

# 검색창에서 키워드 입력 후 엔터
elem = drive.find_element(By.ID,'top_search')
elem.clear()
elem.send_keys(singer)
elem.send_keys(Keys.RETURN)
#time.sleep(3)
# '앨범' 메뉴을 xpath로 찾아 클릭 //*[@id="divCollection"]/ul/li[4]/a/span
album = drive.find_element(By.XPATH, '//*[@id="divCollection"]/ul/li[4]/a/span')
album.click()
time.sleep(2)
# 앨범 이미지를 xpath를 찾아서 입력
drive.find_element(By.XPATH,'//*[@id="frm"]/div/ul/li[1]/div/a[1]').click()

title_list = []
lylic_list = []
song_data = pd.DataFrame()
for i in range(1,5):
    try:
        xp_t=f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[4]/div/div/div[1]/span/a'
        song_title = drive.find_element(By.XPATH, xp_t).text
        title_list.append(song_title)

        xp_s = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[3]/div/a'
        drive.find_element(By.XPATH, xp_s).click()
        song_lylic = drive.find_element(By.ID, 'd_video_summary').text.replace("\n",",")
        lylic_list.append(song_lylic)
        print(song_title, song_lylic)

        drive.back()
        time.sleep(0.5)
    except:
        pass

# print(title_list, lylic_list)
song_data['노래제목']=song_title
song_data['노래가사']=song_lylic
# print(song_data)
song_data.to_excel(singer +'.xlsx', engine='openpyxl')

drive.quit()
