from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signup),
    path('userinfo/',views.userinfo),
    path('userlist/',views.userlist),
    path('userfollow/<int:user_id>/',views.userfollow),
]