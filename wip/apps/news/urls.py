from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.news_feed, name='news_feed'),
    path('create/', views.create, name='create'),
]
