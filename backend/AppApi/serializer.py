from rest_framework import serializers
from blog.models import article


class AppApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        # fields = ('title', 'slug', 'author', 'content', 'publish', 'status')
        exclude = ('created', 'updated')
        # fields = '__all__'
        
