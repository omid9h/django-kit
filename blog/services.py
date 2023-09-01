from blog.models import Post
from kit.services import BaseService


class BlogPostService(BaseService):
    def post_list(self):
        return Post.objects.all()
