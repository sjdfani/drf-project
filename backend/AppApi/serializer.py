from rest_framework import serializers, validators
from blog.models import article
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class AppApiSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = article
        # fields = ('title', 'slug', 'author', 'content', 'publish', 'status')
        exclude = ('created', 'updated')
        # fields = '__all__'

    def validate_title(self, value):
        filter_word = ['java', 'js', 'c#']
        for i in filter_word:
            if i in value:
                raise validators(f"You can't use {i} in your title.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
