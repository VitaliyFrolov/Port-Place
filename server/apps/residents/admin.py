from django.contrib import admin

from server.apps.residents.models import Resident


@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "number",
        "photo",
    )
