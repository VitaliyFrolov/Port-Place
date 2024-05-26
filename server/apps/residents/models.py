from django.db import models
from django_stubs_ext.db.models import TypedModelMeta

from server.apps.residents.const import ResidentStatuses


class Resident(models.Model):
    title: "models.CharField[str, str]" = models.CharField(verbose_name="Название", max_length=100)
    description: "models.CharField[str, str]" = models.CharField(verbose_name="Описание", max_length=150)
    number: "models.CharField[str, str]" = models.CharField(
        verbose_name="Номер телефона", max_length=15, blank=True, null=True
    )
    photo: "models.ImageField[str, str]" = models.ImageField(verbose_name="Фото", upload_to="residents/")
    status: "models.PositiveIntegerField[ResidentStatuses, ResidentStatuses]" = models.PositiveIntegerField(
        verbose_name="Статус", choices=ResidentStatuses, default=ResidentStatuses.in_process
    )

    class Meta(TypedModelMeta):
        verbose_name = "Резидент"
        verbose_name_plural = "Резиденты"

    def __str__(self) -> str:
        return f"{self.title} -- {self.number}"
