from django.contrib import admin

from blog.models import *
from social_media_backend.admin import ManyToManyFieldAdmin


# Register your models here.


class BlogAdmin(ManyToManyFieldAdmin):
    list_display = ["id", "user", "likes", "_tags", "_category", "is_active", "created_at"]
    list_filter = ["user", "tags", "category", "is_active"]
    search_fields = ["title", "content", "user__first_name", "user__id"]
    fields = [
        ("id", "created_at"),
        ("tags", "category"),
        ("is_active", "likes"),
        ("user", ),
        ("title", ),
        ("image_file", "image_caption"),
        ("video", ),
        ("content", ),
    ]
    readonly_fields = ["id", "created_at"]

    def _tags(self, obj):
        return obj.tags.all().values_list("name", flat=True)

    def _category(self, obj):
        return obj.category.all().values_list("name", flat=True)


admin.site.register(Blog, BlogAdmin)
