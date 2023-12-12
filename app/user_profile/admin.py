from django.contrib import admin

from user_profile.models import *

from social_media_backend.admin import ManyToManyFieldAdmin


class TagAdmin(ManyToManyFieldAdmin):
    list_display = ["id", "name", "is_active", "created_at"]
    list_filter = ["is_active"]
    search_fields = ["id", "name"]
    fields = [
        ("id", "created_at"),
        ("name", ),
        ("is_active", )
    ]
    readonly_fields = ["id", "created_at"]


class InterestAdmin(TagAdmin):
    pass


class UserProfileAdmin(ManyToManyFieldAdmin):
    list_display = ["id", "user", "following_count", "_tags", "_interests", "is_active", "created_at"]
    list_filter = ["tags", "interests", "is_active"]
    search_fields = ["id", "name", "user__first_name", "user__last_name", "user__email", "phone_number"]
    fields = [
        ("id", "created_at"),
        ("user", "is_active"),
        ("date_of_birth", "phone_number"),
        ("followings", "following_count"),
        ("image_file", "image_caption"),
        ("tags", "interests")
    ]
    readonly_fields = ["id", "created_at", "following_count"]

    def following_count(self, obj):
        return UserProfile.objects.filter(followings=obj.user).count()

    def _tags(self, obj):
        return list(obj.tags.all().values_list("name", flat=True))

    def _interests(self, obj):
        return list(obj.interests.all().values_list("name", flat=True))


admin.site.register(Tag, TagAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
