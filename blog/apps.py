import inject
from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    def ready(self):
        from .di import di_config

        inject.configure_once(di_config)
