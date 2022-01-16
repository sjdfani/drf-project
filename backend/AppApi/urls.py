from django.urls import path
from .views import ArticleDetail, ArticleList

app_name = 'AppApi'

urlpatterns = [
    path('list/', ArticleList.as_view(), name='list'),
    path('list/<int:pk>', ArticleDetail.as_view(), name='detail'),
]
