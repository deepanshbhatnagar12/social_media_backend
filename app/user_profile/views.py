from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from user_profile.utils import is_email_duplicate
from utilities.views import GeneralPagination


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ["get", "post", "patch"]
    authentication_classes = [TokenAuthentication]
    pagination_class = GeneralPagination

    def update(self, request, *args, **kwargs):
        user_email = request.user.email
        email_id = request.data.get("email")
        # to restrict user to change its email.
        if user_email and email_id:
            request.data.pop("email", None)
        if not user_email and email_id:
            email_id = email_id.lower()
            # Used to check whether the email already exists or not
            if is_email_duplicate(user_email, email_id):
                return Response({"detail": "email already exists"}, status=status.HTTP_400_BAD_REQUEST)

            request.data.update({"email": email_id})

        return super().update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
