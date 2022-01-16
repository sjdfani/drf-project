from blog.models import article
from rest_framework.generics import ListAPIView
from .serializer import AppApiSerializer

class ArticleList(ListAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer