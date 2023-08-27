from inject import Binder

from userprofile.services import ProfileService

__all__ = ["di_config"]


def di_config(binder: Binder) -> None:
    binder.bind(ProfileService, ProfileService())
