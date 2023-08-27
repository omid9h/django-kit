import inject
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from kit.views import BaseAPIView
from userprofile.serializers import AvatarEditSerializer, MeSerializer
from userprofile.services import ProfileService


class AvatarEdit(BaseAPIView):
    """edit (upload) avatar for current logged in user"""

    serializer_class = AvatarEditSerializer
    permission_classes = (IsAuthenticated,)
    service: ProfileService = inject.attr(ProfileService)

    def post(self, request):
        result = self.service.avatar_edit(data=request.data, user=request.user)
        return Response(
            data={
                "username": result.email,
                "avatar": result.avatar.url,
            },
            status=status.HTTP_201_CREATED,
        )


class Me(BaseAPIView):
    """show current user's info"""

    serializer_class = MeSerializer
    permission_classes = (IsAuthenticated,)
    service: ProfileService = inject.attr(ProfileService)

    def get(self, request):
        return Response(data=self.service.me(request.user))
