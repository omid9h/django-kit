from kit.services import BaseService
from kit.utils import remove_field_file
from userprofile import serializers as s


class ProfileService(BaseService):
    def avatar_edit(self, data, user):
        """since the profile has been created when user is created,
        any authenticated user can edit its own profile"""
        serializer = s.AvatarEditSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        current_avatar = user.avatar
        user.avatar = serializer.validated_data["avatar"]
        user.full_clean()
        user.save()
        remove_field_file(current_avatar)
        return user

    def me(self, user):
        serializer = s.MeSerializer(user)
        return serializer.data
