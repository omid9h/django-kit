import inject
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from kit.views import BaseAPIView
from userprofile.serializers import MeSerializer
from userprofile.services import ProfileService


class PostList(BaseAPIView):
    """show filterable posts list"""

    serializer_class = MeSerializer
    permission_classes = (IsAuthenticated,)
    service: ProfileService = inject.attr(ProfileService)

    def get(self, request):
        return Response(data=self.service.me(request.user))
