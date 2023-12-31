from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from user_profile.models import UserProfile, Interest
from user_profile.serializers import UserProfileSerializer, UserSerializer, InterestSerializer, TagSerializer
from user_profile.utils import is_email_duplicate
from utilities.views import GeneralPagination


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    http_method_names = ["post"]
    serializer_class = UserSerializer


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

    def get_object(self):
        if (pk := self.kwargs.get("pk")) == "me":
            return self.request.user.profile
        return super().get_object()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class InterestViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Interest.objects.filter(is_active=True)
    serializer_class = InterestSerializer
    http_method_names = ["get"]
    authentication_classes = [TokenAuthentication]
    pagination_class = GeneralPagination


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Interest.objects.filter(is_active=True)
    serializer_class = TagSerializer
    http_method_names = ["get"]
    authentication_classes = [TokenAuthentication]
    pagination_class = GeneralPagination
