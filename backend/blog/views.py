from django.views.generic import ListView, DetailView
from .models import article
from django.shortcuts import get_object_or_404


class article_list(ListView):
    template_name = "blog/article_list.html"

    def get_queryset(self):
        return article.objects.filter(status=True)


class ArticaleDetailView(DetailView):
    def get_queryset(self):
        return get_object_or_404(
            article.objects.filter(status=True),
            pk=self.kwargs.get("pk")
        )
