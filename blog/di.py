from inject import Binder

from . import services as s

__all__ = ["di_config"]


def di_config(binder: Binder) -> None:
    binder.bind(s.BlogPostService, s.BlogPostService())
