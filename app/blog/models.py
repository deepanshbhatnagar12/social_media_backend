from django.contrib.auth.models import User
from django.db import models

from user_profile.models import Tag, Interest
from utilities.models import BaseModelWithCreatedInfo, BaseImageModel, get_video_file_path


class Blog(BaseModelWithCreatedInfo, BaseImageModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_blogs")
    likes = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    video = models.FileField(null=True, blank=True, upload_to=get_video_file_path)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tag_blogs")
    category = models.ManyToManyField(Interest, blank=True, related_name="interest_blogs")
    is_active = models.BooleanField(default=True)
