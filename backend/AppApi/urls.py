from django.urls import path
from .views import ArticleDetail, ArticleList,UserList,UserDetail

app_name = 'AppApi'

urlpatterns = [
    path('list/', ArticleList.as_view(), name='list'),
    path('list/<int:pk>', ArticleDetail.as_view(), name='detail'),
    path('list/', UserList.as_view(), name='list_user'),
    path('list/<int:pk>', UserDetail.as_view(), name='detail_user'),
]
