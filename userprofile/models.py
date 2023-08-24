from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy

from kit import validators as v
from kit.utils import generate_uuid_for_file_with_dir


def generate_uuid_for_author_avatar(_, original_file_name: str):
    return generate_uuid_for_file_with_dir(
        original_file_name,
        settings.USERPROFILE_AVATAR_DIR,
    )


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(gettext_lazy("Bio"))
    avatar = models.ImageField(
        gettext_lazy("Avatar"),
        upload_to=generate_uuid_for_author_avatar,
        blank=True,
        null=True,
        validators=[
            v.FileSizeValidator(settings.CUSTOMER_AVATAR_MAX_SIZE),
            v.FileExtensionValidator(settings.CUSTOMER_AVATAR_ALLOWED_EX),
        ],
    )
