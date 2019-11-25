import requests
import time
import csv
from bs4 import BeautifulSoup
from decouple import config
import requests

def send_naver_movie(movie_name):
    naver_client_id = config('NAVER_CLIENT_ID')
    naver_client_secret = config('NAVER_CLIENT_SECRET')
    BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'  # 상수를 의미할 때는(절대 안바뀔것같은 경우) 대문자로 변수 이름을 보통 짓는다. => 재할당하면 안돼! 의미 
    URL = BASE_URL + '?query=' + movie_name

    headers = {
        'X-Naver-Client-Id' : naver_client_id,
        'X-Naver-Client-Secret' : naver_client_secret,
    }

    response = requests.get(URL, headers=headers)  # 원본이 바뀌지 않고 return 값이 있다. 
    return response.json()  # class : dict



# boxoffice.csv 에서 영화명(국문) 가져오기 
with open('result.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    movie_names = []
    for row in reader:
        movie_names.append(row['movieNm']) 


# boxoffice.csv 에서 무비코드 가져오기
with open('result.csv', 'r', encoding='utf-8') as f1:
    reader = csv.DictReader(f1)
    movie_codes = []
    for row in reader:
        movie_codes.append(row['movieCd']) 


# # csv 만들기
# with open('plusUrl.csv', 'w', encoding='utf-8', newline='') as f2:
#     fieldnames = ['movieCd', 'image_url', 'userRating', 'link']
#     writer = csv.DictWriter(f2, fieldnames=fieldnames)
#     writer.writeheader()

# # 네이버 API 에 넣어서 데이터 가져오기 
#     result_1 = {}
#     for movie_name in movie_names:
#         time.sleep(0.5)  # 0.5초씩 쉬면서 for문을 돌게 해준다.
        
#         data = send_naver_movie(movie_name)['items'][0]

#         result_1['userRating'] = data['userRating']
#         # result_1['channel'] = data['channel']
#         # index 사용하여 무비네임스에서 인덱스 같게 해서 
#         result_1['movieCd'] = movie_codes[movie_names.index(movie_name)]
#         result_1['link'] = data['link']

#         # 썸네일 이미지 url 이 없는 경우 대비
#         if data['image']:
#             result_1['image_url'] = data['image']

#         writer.writerow(result_1)

with open('plusUrl.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    movie_links = []
    for row in reader:
        movie_links.append(row['link'])

with open('movie_des.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd','description']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    res = {}
    idx = 0
    for movie_name in movie_names:
        for _ in range(len(movie_links)):
            
            url = f'{movie_links[idx]}'
            idx += 1
            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')
            dss = soup.find('p',{'class':'con_tx'})
            dss_text = dss.getText()
            # dss = soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div > p.con_tx')
            
            res['movieCd'] = movie_codes[movie_names.index(movie_name)]
            res['description'] = dss_text
            writer.writerow(res)
            break
