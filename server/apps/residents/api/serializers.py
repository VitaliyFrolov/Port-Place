from django_stubs_ext.db.models import TypedModelMeta
from rest_framework import serializers

from server.apps.residents.models import Resident


class ResidentSerializer(serializers.ModelSerializer[Resident]):
    status = serializers.CharField(source="get_status_display")

    class Meta(TypedModelMeta):
        model = Resident
        fields = (
            "title",
            "description",
            "number",
            "photo",
            "status",
        )


class ResidentCreateSerializer(serializers.ModelSerializer[Resident]):
    class Meta(TypedModelMeta):
        model = Resident
        fields = (
            "title",
            "description",
            "number",
            "photo",
            "status",
        )
