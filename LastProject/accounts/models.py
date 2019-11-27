from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField()

    gender = models.CharField(max_length=1, choices=((('M', '남성(Male)'), ('F', '여성(Female)'))))
    kakao_id = models.CharField(max_length=50)

    stars = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='fans')
    
    def get_absolute_url(self):
        return reverse("accounts:user_detail", kwargs={"user_id": self.pk})