from django.utils.translation import gettext_lazy
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView


class BaseAPIView(APIView):
    """base API view for all other API views"""


class FilteredAPIView(BaseAPIView):
    """filtered API view when we want filtering via query params and using `django-filter` on querysets"""

    def filtered_queryset(
        self, query_params, queryset=None, raise_exception=False, **kwargs
    ):
        filterset = self.filterset_class(query_params, queryset, **kwargs)
        if raise_exception and not filterset.is_valid():
            raise ValidationError({gettext_lazy("filterset errors"): filterset.errors})
        return filterset.qs
