from django.urls import path
from .views import index, add, all, search, delete, edit
# define some patterns for urls for my project

urlpatterns = [
    # app paths
    path("", index, name="home"),
    path('add', add, name="addWord"),
    path('all/', all, name="allWords"),
    path('search/', search, name="Search"),
    path('delete/', delete, name="Delete"),
    path('edit/<int:word_id>/', edit, name="Edit"),
]