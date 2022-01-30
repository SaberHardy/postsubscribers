from django.contrib import admin
from blog.models import Post, Comment


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_created']


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)
