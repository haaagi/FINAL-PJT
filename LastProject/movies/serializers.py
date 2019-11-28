from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review, Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','movie_code','rank','audience','title','title_eng','open_date','genre1','genre2','genre3','watch_grade','poster_url','user_rating','naver_link','description','like_users')


class ReviewCreationSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=True)
    class Meta:
        model = Review
        fields = ('id','content','score',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)
    class Meta: 
        model = Movie
        fields = ('id', 'review_set',)