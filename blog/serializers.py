from rest_framework import serializers

from . import models as m


class PostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Post
        fields = "__all__"
