from rest_framework import serializers

from kit.models import User


class AvatarEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("avatar",)
        extra_kwargs = {"avatar": {"required": True, "allow_null": False}}


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "avatar",
        )
