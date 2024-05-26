from django.urls import path

from server.apps.residents.api.views import (
    ResidentCreateAPIView,
    ResidentDetailAPIView,
    ResidentsListAPIView,
)

app_name = "residents"

urlpatterns = [
    path("", ResidentsListAPIView.as_view(), name="residents-list"),
    path("<int:pk>/", ResidentDetailAPIView.as_view(), name="resident-detail"),
    path("create/", ResidentCreateAPIView.as_view(), name="resident-create"),
]
