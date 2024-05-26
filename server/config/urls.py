from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        f"{settings.API_PREFIX}/residents/",
        include("server.apps.residents.api.urls", namespace="residents"),
    ),
]
