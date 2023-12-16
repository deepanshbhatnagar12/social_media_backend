from django.contrib.auth.models import User
from rest_framework import serializers

from user_profile.models import UserProfile
from user_profile import constants as user_management_constants


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "is_active", "username"]


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email", required=False, max_length=100, allow_blank=True)
    first_name = serializers.CharField(source="user.first_name", required=False, max_length=100, allow_blank=True)
    last_name = serializers.CharField(source="user.last_name", required=False, max_length=100, allow_blank=True)

    class Meta:
        model = UserProfile
        exclude = []

    def update(self, instance, validated_data):
        """
        Override update functionality to achieve the following:
            * Update instance's user details if received.
            * Check if user has completed signup progress and trigger Sign-Up email to user's updated email.
        """
        # fetch user's email from the pre-updated state
        email = instance.user.email
        # updating instance's user
        if validated_data.get("user"):
            user_instance = UserSerializer(instance=instance.user, data=validated_data["user"], partial=True)
            user_instance.is_valid(raise_exception=True)
            user_instance.save()
            validated_data["user"] = instance.user
        updated_email = instance.user.email
        # Check if user's email is being updated for the first time(which denotes user has completed its signup)
        # Trigger Sign-Up email to user's updated email at that instant.
        if not email and updated_email:
            pass
        #     send_mail_using_templates(
        #         user_management_constants.SUBJECT_SIGNUP_OTP_EMAIL,
        #         user_management_constants.TEMPLATE_CONTENT_EMAIL_WITH_NAME,
        #         context={
        #             "name": instance.user.get_full_name(),
        #             "content": user_management_constants.SUBJECT_SIGNUP_OTP_EMAIL,
        #         },
        #         to_email=instance.user.email,
        #     )

        return super(UserProfileSerializer, self).update(instance, validated_data)