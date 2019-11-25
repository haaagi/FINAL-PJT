import requests
from decouple import config
from datetime import datetime, timedelta
import csv
import pandas as pd
API_KEY = config('API_KEY')



# URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&weekGb=0&targetDt='


# movie_code = []

# with open ('boxoffice.csv', 'w' , encoding ='utf-8', newline='') as f:
    
    
#     fieldnames = ['movieCd','rank', 'audiAcc']
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     for i in range(0,80):
        
#         k = datetime(2019, 11, 23) - timedelta(weeks=i)

#         data = requests.get(URL+k.strftime('%Y%m%d')).json()

#         for movie in data.get('boxOfficeResult').get('weeklyBoxOfficeList'):
#             if not movie.get('movieCd') in movie_code:
#                 writer.writerow({'movieCd':movie.get('movieCd'),'rank':movie.get('rank'),'audiAcc':movie.get('audiAcc')})
#                 movie_code.append(movie.get('movieCd'))
#             else:
#                 pass
                   
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd='

# csv에서 무비 코드만 가져오기 
with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    movie_codes = []
    for row in reader:
        movie_codes.append(row['movieCd'])

# csv 만들기
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd','movieNm','movieNmEn', 'openDt', 'genre1','genre2','genre3', 'audits']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    result = {} 
    for cod in movie_codes:
        data = requests.get(URL+cod).json()
        result['movieCd'] = data['movieInfoResult']['movieInfo']['movieCd']
        result['movieNm'] = data['movieInfoResult']['movieInfo']['movieNm']
        result['movieNmEn'] = data['movieInfoResult']['movieInfo']['movieNmEn']
        result['openDt'] = data['movieInfoResult']['movieInfo']['openDt']
        genres_cnt = len(data['movieInfoResult']['movieInfo']['genres'])
        if genres_cnt == 1: 
            result['genre1'] = data['movieInfoResult']['movieInfo']['genres'][0]['genreNm']
        elif genres_cnt == 2:
            result['genre1'] = data['movieInfoResult']['movieInfo']['genres'][0]['genreNm']
            result['genre2'] = data['movieInfoResult']['movieInfo']['genres'][1]['genreNm']
        else:
            result['genre1'] = data['movieInfoResult']['movieInfo']['genres'][0]['genreNm']
            result['genre2'] = data['movieInfoResult']['movieInfo']['genres'][1]['genreNm']
            result['genre3'] = data['movieInfoResult']['movieInfo']['genres'][2]['genreNm']
        if data['movieInfoResult']['movieInfo']['audits']:
            result['audits'] = data['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm']
        writer.writerow(result)


a = pd.read_csv('boxoffice.csv')
b = pd.read_csv('movie.csv')
result = a.merge(b, on='movieCd')
result.to_csv("result.csv", index=False)