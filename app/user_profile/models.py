from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from utilities.models import BaseModelWithCreatedInfo, BaseModelWithUniqueName, BaseImageModel


class Tag(BaseModelWithUniqueName):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Interest(BaseModelWithUniqueName):
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class UserProfile(BaseModelWithCreatedInfo, BaseImageModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    followings = models.ManyToManyField(User, blank=True, related_name="followers")
    phone_number = PhoneNumberField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="tag_profiles")
    interests = models.ManyToManyField(Interest, blank=True, related_name="interest_profiles")
    is_active = models.BooleanField(default=True)


