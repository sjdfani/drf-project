from django.urls import path
from .views import ArticaleDetail, ArticaleList, ArticaleUpdate, ArticaleDelete, ArticaleCreate, UserList, UserDetail

app_name = 'AppApi'

urlpatterns = [
    path('articale-create/', ArticaleCreate.as_view(), name='create'),
    path('articale-list/', ArticaleList.as_view(), name='list'),
    path('articale-list/<int:pk>', ArticaleDetail.as_view(), name='detail'),
    # path('list/<slug:slug>', ArticleDetail.as_view(), name='detail'),
    path('articale-list/<int:pk>/update',
         ArticaleUpdate.as_view(), name='update'),
    path('articale-list/<int:pk>/delete',
         ArticaleDelete.as_view(), name="delete"),
    # =========================================================================
    path('user/', UserList.as_view(), name='list_user'),
    path('user/<int:pk>', UserDetail.as_view(), name='detail_user'),
]
