from django.urls import path
from . import views

# app_name = 'tweet'

urlpatterns = [
   path('', views.list_tweets, name='list_tweets'),
   path('create/', views.create_tweet, name='create_tweet'),
   path('<int:tweet_id>/edit/', views.edit_tweet, name='edit_tweet'),
   path('<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'),
   path('register/', views.register, name='register'),
]