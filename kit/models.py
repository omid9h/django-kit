import uuid

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
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


class KitUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        (username is omitted)
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    user model explicitly implemented for future enhancements
    """

    username = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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

    objects = KitUserManager()
