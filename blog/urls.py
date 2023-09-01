from django.urls import path

from . import views as v

app_name = "userprofile"

urlpatterns = [
    path("", v.PostsList.as_view(), name="posts_list"),
]
