from rest_framework import serializers
from blog.models import article


class AppApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = "__all__"
