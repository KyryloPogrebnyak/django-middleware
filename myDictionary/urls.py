from django.urls import path
from . import views
# define some patterns for urls for my project

urlpatterns = [
    # app paths
    path("", views.index, name="home"),
    path("add/", views.add, name="add")
]