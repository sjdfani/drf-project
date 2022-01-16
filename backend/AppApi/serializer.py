from rest_framework import serializers
from blog.models import article
from django.contrib.auth.models import User


class AppApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        # fields = ('title', 'slug', 'author', 'content', 'publish', 'status')
        exclude = ('created', 'updated')
        # fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
