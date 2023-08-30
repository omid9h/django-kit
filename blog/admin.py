from django.contrib import admin

from blog import models as m

admin.site.register(m.Author)
admin.site.register(m.Post)
admin.site.register(m.Comment)
