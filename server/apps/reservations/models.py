from typing import TYPE_CHECKING

from django.db import models
from django_stubs_ext.db.models import TypedModelMeta

if TYPE_CHECKING:
    from datetime import datetime

    from server.apps.tables.models import Table


class Reservation(models.Model):
    table: "models.ForeignKey[Table | None, Table | None]" = models.ForeignKey(
        "tables.Table", on_delete=models.SET_NULL, null=True
    )
    guest_name: "models.CharField[str, str]" = models.CharField(verbose_name="Имя гостя", max_length=50, blank=True)
    guest_phone: "models.CharField[str, str]" = models.CharField(verbose_name="Номер гостя", max_length=20, blank=True)
    start: "models.DateTimeField[datetime, datetime]" = models.DateTimeField(verbose_name="Начало")
    end: "models.DateTimeField[datetime, datetime]" = models.DateTimeField(verbose_name="Конец")

    class Meta(TypedModelMeta):
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
        default_related_name = "reservations"
        constraints = [
            models.CheckConstraint(
                check=models.Q(start__lt=models.F("end")),
                name="%(app_label)s_%(class)s_end_gt_start",
            ),
            models.CheckConstraint(
                check=models.Q(start__isnull=True, end__isnull=True) | models.Q(start__isnull=False, end__isnull=False),
                name="%(app_label)s_%(class)s_end_start_both_or_none",
            ),
        ]

    def __str__(self) -> str:
        return f"Table {self.table} -- {self.guest_name} - {self.guest_phone}"
