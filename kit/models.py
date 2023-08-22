from django.db import models


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
