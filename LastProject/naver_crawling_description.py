# import bs4
# import requests
# import csv

# url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=189053'

# headers = {'User-Agent': ':)'} 
# #사용자의 요원이다. 우리 대신해서 요청을 보내는 사람을 쓰라는 것. 
# #약간의 변형이 필요한 경우도 있다. 

# response = requests.get(url, headers=headers).text
# text = bs4.BeautifulSoup(response, 'html.parser')
# # rows = text.select('.lst50')

# writer = csv.writer(open('test_ds.csv', 'w', encoding='utf-8', newline=''))
# writer.writerow(['ds'])

# # for row in rows:
# rank = select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div > p').text
#     # title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
#     # artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
# writer.writerow([ds])


import requests
from bs4 import BeautifulSoup
import csv

with open('test_result.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    movie_codes = []
    for row in reader:
        movie_codes.append(row['movieCd']) 


with open('test_movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    movie_links = []
    for row in reader:
        movie_links.append(row['link'])

with open('test_movie_ds.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd','description']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

    res = {}

    for link in movie_links:

        url = f'{link}'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        dss = soup.select('#content > div.article > div.section_group.section_group_frst > div:nth-child(1) > div > div > p.con_tx')

        res['description'] = dss
        res['movieCd'] = movie_codes[movie_names.index(movie_name)]

        writer.writerow(res)

