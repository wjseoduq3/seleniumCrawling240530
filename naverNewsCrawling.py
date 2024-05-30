import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

url='https://news.naver.com/breakingnews/section/101/259'
header={'user-agent':'Mozilla/5.0'}
res=requests.get(url, headers=header)
soup= BeautifulSoup(res.text,'lxml')

# print(soup)
news_list=[]
tag3=soup.find('ul',{'class':'sa_list'}).find_all('li', limit=3)
for li in tag3:
    news_info={'title':li.find('strong',{'class':'sa_text_strong'}).text,
              'news_url':li.find('a')['href']}
    news_list.append(news_info)
# print(news_list)

for news in news_list:
    de_url =news['news_url']
    de_res = requests.get(de_url, headers=header)
    de_soup = BeautifulSoup(de_res.text, 'lxml')
    print(de_url)

    body = de_soup.find('article',{'class':'go_trans _article_content'})
    news_contents = body.text.replace('\n','').strip()
    news['news_contents']=news_contents

df = pd.DataFrame(news_list)
# print(df)
# print(news_list)

# 한 줄 요약
# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY = 'APIKey'

# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens = 1, temperature = 1.0, top_p = 1.0, n = 1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

#koGPT에 전달할 명령어
for i in range(len(df['news_contents'])):
    #try:
        prompt = df['news_contents'].iloc[i]
        # print(prompt)
        response = kogpt_api(prompt, max_tokens=200, top_p=0.7)
        # print(response)
        summ = response['generations'][0]['text']
        # print(summ)
print(df)
        #df['summary'].iloc[i] = summ
    # except:
    #     pass
        #print(type(response))
print(df)
