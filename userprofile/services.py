from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils.translation import gettext_lazy

from kit.services import BaseService
from kit.utils import remove_field_file
from userprofile import serializers as s


class ProfileService(BaseService):
    def avatar_edit(self, data, user):
        """since the profile has been created when user is created,
        any authenticated user can edit its own profile"""
        serializer = s.AvatarEditSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        try:
            m = get_user_model().objects.get(Q(pk=user.id) & Q(is_active=True))
        except get_user_model().DoesNotExist:
            raise ValueError(gettext_lazy("Customer does not exist"))
        current_avatar = m.avatar
        m.avatar = serializer.validated_data["avatar"]
        m.full_clean()
        m.save()
        remove_field_file(current_avatar)
        return m

    def me(self, user):
        serializer = s.MeSerializer(user)
        return serializer.data
