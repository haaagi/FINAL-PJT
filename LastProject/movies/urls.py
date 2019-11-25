from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.movielist),

]