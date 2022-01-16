from django.views.generic import ListView
from .models import article


class article_list(ListView):
    template_name = "blog/article_list.html"

    def get_queryset(self):
        return article.objects.filter(status=True)
