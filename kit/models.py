import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy

from kit import validators as v
from kit.utils import generate_uuid_for_file_with_dir


class BaseModel(models.Model):
    """
    base model for all other models
    """

    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def full_clean_and_save(
        self,
        exclude=None,
        validate_unique=True,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        self.full_clean(exclude, validate_unique)
        self.save(force_insert, force_update, using, update_fields)


def generate_uuid_for_user_avatar(_, original_file_name: str):
    return generate_uuid_for_file_with_dir(
        original_file_name,
        settings.USERPROFILE_AVATAR_DIR,
    )


class User(AbstractUser):
    """
    user model explicitly implemented for future enhancements
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(gettext_lazy("email address"), unique=True, blank=True)
    avatar = models.ImageField(
        gettext_lazy("avatar"),
        upload_to=generate_uuid_for_user_avatar,
        blank=True,
        null=True,
        validators=[
            v.FileSizeValidator(settings.USERPROFILE_AVATAR_MAX_SIZE),
            v.FileExtensionValidator(settings.USERPROFILE_AVATAR_ALLOWED_EX),
        ],
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
