from django.urls import path

from . import views as v

app_name = "userprofile"

urlpatterns = [
    path("", v.Me.as_view(), name="me"),
    path("avatar/", v.AvatarEdit.as_view(), name="avatar"),
]
