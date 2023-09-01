import django_filters as f

from blog import models as m


class PostFilter(f.FilterSet):
    author = f.ModelChoiceFilter(queryset=m.Author.objects.all())
    title = f.CharFilter(field_name="title", lookup_expr="icontains")
    content = f.CharFilter(field_name="content", lookup_expr="icontains")

    class Meta:
        model = m.Post
        fields = ["author", "title", "content"]
