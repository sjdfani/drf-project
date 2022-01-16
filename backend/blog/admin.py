from django.contrib import admin
from .models import article


@admin.register(article)
class Article(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish', 'created', 'updated', 'status')
    list_editable = ('status',)
    list_filter = ('author',)
