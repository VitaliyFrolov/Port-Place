from rest_framework import generics

from server.apps.residents.api.serializers import (
    ResidentCreateSerializer,
    ResidentSerializer,
)
from server.apps.residents.models import Resident


class ResidentsListAPIView(generics.ListAPIView[Resident]):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer


class ResidentDetailAPIView(generics.RetrieveAPIView[Resident]):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer


class ResidentCreateAPIView(generics.CreateAPIView[Resident]):
    queryset = Resident.objects.all()
    serializer_class = ResidentCreateSerializer
