from django.contrib import admin

from blog.models import BlogPost, PostInfo


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "creation_date", "publication_sign", "number_of_views")
    search_fields = ("title", "creation_date")

@admin.register(PostInfo)
class BlogInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "creation_date", "publication_sign", "number_of_views")
    search_fields = ("title", "creation_date")

