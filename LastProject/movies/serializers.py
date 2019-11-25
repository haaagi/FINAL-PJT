from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Review



class ReviewSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=True)
    class Meta:
        model = Review
        fields = ('id','user','movie','content','score',)