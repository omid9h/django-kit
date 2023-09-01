import inject
from rest_framework.permissions import AllowAny

from blog.filtersets import PostFilter
from kit.paginations import LimitOffsetPagination, get_paginated_response
from kit.views import FilteredAPIView

from . import serializers as z
from . import services as s


class PostsList(FilteredAPIView):
    """show filterable posts list"""

    # serializer_class = ...
    permission_classes = (AllowAny,)
    filterset_class = PostFilter
    service: s.BlogPostService = inject.attr(s.BlogPostService)

    def get(self, request):
        return get_paginated_response(
            pagination_class=LimitOffsetPagination,
            serializer_class=z.PostsListSerializer,
            queryset=self.filtered_queryset(request.GET, self.service.post_list()),
            request=request,
            view=self,
        )
