"""social_media_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from rest_auth.views import LoginView
from rest_framework_nested.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
schema_view = get_swagger_view(title="social_media_backend APIS")

urlpatterns = [
    url(r"swagger/", schema_view),
    path("api/v1/", include(router.urls)),
    url(r"^jet/", include("jet.urls", "jet")),  # Django JET URLS
    url(r"^jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),  # Django JET dashboard URLS
    path("api/v1/rest-auth/login/", csrf_exempt(LoginView.as_view()), name="rest_login"),
    path("api/v1/rest-auth/", include("rest_auth.urls")),
    path("_nested_admin/", include("nested_admin.urls")),
    path("api/v1/", include("utilities.urls")),
    path("", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


