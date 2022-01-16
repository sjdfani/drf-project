from django.urls import path
from .views import article_list

app_name = 'blog'

urlpatterns = [
    path('articles/', article_list.as_view(), name="articles"),
]
