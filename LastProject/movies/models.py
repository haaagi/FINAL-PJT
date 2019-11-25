from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
import json
import csv

User = get_user_model()

class Movie(models.Model):
    movie_code = models.IntegerField()
    rank = models.IntegerField()
    audience = models.IntegerField()
    title = models.CharField(max_length=50)
    title_eng = models.CharField(max_length=50)
    open_date = models.CharField(max_length=100)
    genre1 = models.CharField(max_length=30)
    genre2 = models.CharField(max_length=30,blank=True)
    genre3 = models.CharField(max_length=30,blank=True)
    watch_grade = models.CharField(max_length=50)
    poster_url = models.CharField(max_length=200)
    user_rating = models.FloatField()
    naver_link = models.CharField(max_length=100)
    description = models.TextField()

    like_users = models.ManyToManyField(User, related_name='like_movies')


    def get_absolute_url(self):
        return reverse("movies:movie_detail", kwargs={"movie_id": self.pk})

    @classmethod
    def import_data(cls):
        import os
        # path = os.path.join(os.getcwd(), 'fixtures', 'data2.json')
        with open('./movies/fixtures/data2.json', 'r', encoding='utf-8') as f:
            movies = json.load(f)
            for movie in movies:
                cls.objects.create(
                    movie_code = int(movie['movieCd']),
                    rank = int(movie['rank']),
                    audience = int(movie['audiAcc']),
                    title = movie['movieNm'],
                    title_eng = movie['movieNmEn'],
                    open_date = movie['openDt'],
                    genre1 = movie['genre1'],
                    genre2 = movie['genre2'],
                    genre3 = movie['genre3'],
                    watch_grade = movie['audits'],
                    poster_url = movie['image_url'],
                    user_rating = float(movie['userRating']),
                    naver_link = movie['link'],
                    description = movie['description']
                )
    
class Review(models.Model):
    content = models.CharField(max_length=140)
    score = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)