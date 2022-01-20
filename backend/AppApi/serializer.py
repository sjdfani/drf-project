from rest_framework import serializers, validators
from blog.models import article
from django.contrib.auth import get_user_model


class AuthorRelated(serializers.RelatedField):
    def to_representation(self, value):
        return value.username
        # return f"{value.first_name} {value.last_name}"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'first_name', 'last_name']


class AppApiSerializer(serializers.ModelSerializer):

    def get_author(self, obj):
        # return obj.author.username
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
        }

    # author = AuthorSerializer() # with class
    # author = serializers.HyperlinkedIdentityField(view_name='AppApi:authors') #send id to url and get data of class in veiw
    # author = AuthorRelated(read_only=True) # with class
    # author = serializers.CharField(source="author.username", read_only=True) #alone
    author = serializers.SerializerMethodField("get_author")  # with func

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
        model = get_user_model()
        fields = '__all__'
