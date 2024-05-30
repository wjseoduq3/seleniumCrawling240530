import requests
import json

# 다음 검색
url = "https://dapi.kakao.com/v2/search/web"
# 1-1. url_get = "https://dapi.kakao.com/v2/search/web?query=인공지능"
rest_api_key = 'jdy23d40a45b6dab00ad785dd41e579e41a'
my_headers = {"Authorization": "KakaoAK "+rest_api_key}
req_params = {'query':'인공지능', 'sort':'accuracy', 'page':1, 'size':30}

r = requests.get(url,params=req_params,headers=my_headers)
# 1-2. r = requests.get(url,headers=my_headers) 1-1.과 한 쌍

# print(r.status_code)
# print(r.url)
# print(r.json())
# print(r['documents':[[{'contents': '<b>인공지능</b>(人工智能, Artificial Intelligence)은 인간의 <b>지능</b>이 가지는 학습, 추리, 적응, 논증 따위의 기능을 갖춘 컴퓨터 시스템을 의미한다. 인간의 학습능력, 추론능력, 지각능력을 <b>인공</b>적으로 구현시키는...', 'datetime': '2024-05-23T00:00:00.000+09:00', 'title': '<b>인공지능</b> - 나무위키', 'url': 'https://namu.wiki/w/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'}, {'contents': '서울<b>인공지능</b>고등학교는 서울특별시 송파구 거여동에 위치한 공립 특성화고등학교로 AI컴퓨터과, AI전자과 , 전기에너지과, 하이텍디자인과 총 4개과가 있다. 서울특별시교육청으로부터 2021년 &#39;AI분야 특성화...', 'datetime': '2024-05-10T00:00:00.000+09:00', 'title': '서울<b>인공지능</b>고등학교 - 나무위키', 'url': 'https://namu.wiki/w/%EC%84%9C%EC%9A%B8%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90'}, {'contents': '김상윤 중앙대 컴퓨터공학과 교수 경남경총 노사합동 세미나서 강연 “핵심 역량 <b>인공지능</b>에 내주는 시대 일을 잘 시키는 역량이 주목받아”     “기술적으로는 <b>인공지능</b> 변호사가 이미 탄생했습니다. 우리 산업...', 'datetime': '2024-05-22T21:50:40.000+09:00', 'title': '“<b>인공지능</b>이 올해 말 세상 바꾼다… 데이터 구축 가장 중요” - 콘텐츠뷰', 'url': 'https://v.daum.net/v/4hyTNdmeqX'}], 'meta': {'is_end': False, 'pageable_count': 971, 'total_count': 2763202}}
# ]])
result = r.json()
# print(len(result['documents']))
for i in range(1, 30):
    print(result['documents'][i]['contents'])


