from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from blog.models import Blog
from blog.serializers import BlogSerializer
from user_profile.models import UserProfile
from utilities.views import GeneralPagination


class BlogViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BlogSerializer
    http_method_names = ["get", "post", "patch"]
    authentication_classes = [TokenAuthentication]
    pagination_class = GeneralPagination

    def list(self, request, *args, **kwargs):
        inactive_blogs = bool(self.request.query_params.get("inactive", False))
        if inactive_blogs is True:
            queryset_inactive = BlogSerializer(self.queryset.filter(user=self.request.user, is_active=False), many=True).data
            return Response(queryset_inactive, status=status.HTTP_200_OK)
        my_blogs = bool(self.request.query_params.get("my_blogs", False))
        queryset = self.queryset.filter(is_active=True)
        if my_blogs is True:
            queryset = queryset.filter(user=self.request.user)

        followed = bool(self.request.query_params.get("followed", False))
        if followed is True:
            followed_users = UserProfile.objects.filter(followings=self.request.user).values_list("user", flat=True)
            queryset = queryset.filter(user__id__in=followed_users)

        queryset_serialized = BlogSerializer(queryset, many=True).data
        return Response(queryset_serialized, status=status.HTTP_200_OK)
