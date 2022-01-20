from django.urls import path, include
# from .views import ArticleDetail, ArticleList, ArticleUpdate, ArticleDelete, ArticleCreate, UserList, UserDetail, ArticleAll
from rest_framework import routers
from .views import UserViewSet, ArticleViewSet

app_name = 'AppApi'

# urlpatterns = [
#     path('article-create/', ArticleCreate.as_view(), name='create'),
#     path('article-list/', ArticleList.as_view(), name='list'),
#     path('article-list/<int:pk>', ArticleDetail.as_view(), name='detail'),
#     # path('list/<slug:slug>', ArticleDetail.as_view(), name='detail'),
#     path('article-list/<int:pk>/update',
#          ArticleUpdate.as_view(), name='update'),
#     path('article-list/<int:pk>/delete',
#          ArticleDelete.as_view(), name="delete"),
#     path('article-list/<int:pk>/all',
#          ArticleAll.as_view(), name="all"),
#     # =========================================================================
#     path('user/', UserList.as_view(), name='list_user'),
#     path('user/<int:pk>', UserDetail.as_view(), name='detail_user'),
# ]

router = routers.SimpleRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('users', UserViewSet, basename='users')

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]
