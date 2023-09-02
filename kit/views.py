import logging

from django.conf import settings
from django.utils.translation import gettext_lazy
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from kit.serializers import AuthTokenSerializer

project_logger = logging.getLogger(settings.PROJECT_LOGGER)


class BaseAPIView(APIView):
    """base API view for all other API views"""


class FilteredAPIView(BaseAPIView):
    """filtered API view when we want filtering
    via query params and using `django-filter` on querysets"""

    def filtered_queryset(self, query_params, queryset=None, raise_exception=False, **kwargs):
        filterset = self.filterset_class(query_params, queryset, **kwargs)
        if raise_exception and not filterset.is_valid():
            raise ValidationError({gettext_lazy("filterset errors"): filterset.errors})
        return filterset.qs


class CreateToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class Index(BaseAPIView):
    """simple index/home view"""

    def get(self, request):
        # just for testing logging
        project_logger.info("index request: %r", request)
        return Response(data={"message": "index"})
