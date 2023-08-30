from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy

from kit.models import BaseModel


class Author(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)


class Post(BaseModel):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author_posts")
    title = models.CharField(gettext_lazy("title"), max_length=200, null=False, blank=False)
    content = models.TextField(gettext_lazy("content"), null=False, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=["title"]),
            models.Index(fields=["content"]),
        ]


class Comment(BaseModel):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="user_comments",
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    content = models.TextField(gettext_lazy("content"), null=False, blank=False)
