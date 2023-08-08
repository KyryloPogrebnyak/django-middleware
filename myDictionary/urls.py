from django.urls import path
from .views import index
# define some patterns for urls for my project

urlpatterns = [
    # app paths
    path("", index, name="home")
]