from blog.models import article
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializer import AppApiSerializer, UserSerializer


class ArticleList(ListAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
