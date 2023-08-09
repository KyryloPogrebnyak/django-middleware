from django.urls import path
from . import views
# define some patterns for urls for my project

urlpatterns = [
    path("", views.index, name="home"),
    path("add/", views.add, name="add"),
    path("word/all/", views.all_words, name="all_words"),
    path("search/", views.search, name="search"),  
]