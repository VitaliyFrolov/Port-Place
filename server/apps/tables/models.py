from django.db import models
from django_stubs_ext.db.models import TypedModelMeta

from server.apps.tables.const import TableType


class Table(models.Model):
    number: "models.PositiveSmallIntegerField[int, int]" = models.PositiveSmallIntegerField(
        verbose_name="Номер стола", primary_key=True
    )
    table_type: "models.PositiveSmallIntegerField[int, int]" = models.PositiveSmallIntegerField(
        verbose_name="Тип стола", choices=TableType.choices
    )

    class Meta(TypedModelMeta):
        verbose_name = "Стол"
        verbose_name_plural = "Столы"

    def __str__(self) -> str:
        return f"{self.number} -- {self.table_type}"
