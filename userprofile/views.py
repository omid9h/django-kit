from rest_framework.permissions import IsAuthenticated

from kit.views import BaseAPIView


class ProfileCreate(BaseAPIView):
    """creates profile attached to its user who calls it"""

    permission_classes = (IsAuthenticated,)
