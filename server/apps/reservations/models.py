from typing import TYPE_CHECKING

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta

if TYPE_CHECKING:
    from datetime import datetime

    from server.apps.tables.models import Table


class Reservation(models.Model):
    table: "models.ForeignKey[Table | None, Table | None]" = models.ForeignKey(
        "tables.Table", on_delete=models.SET_NULL, null=True
    )
    guest_name: "models.CharField[str, str]" = models.CharField(verbose_name=_("Guest name"), max_length=50, blank=True)
    guest_phone: "models.CharField[str, str]" = models.CharField(
        verbose_name=_("Guest phone"), max_length=20, blank=True
    )
    start: "models.DateTimeField[datetime, datetime]" = models.DateTimeField(verbose_name=_("Start of reservation"))
    end: "models.DateTimeField[datetime, datetime]" = models.DateTimeField(verbose_name=_("End of reservation"))

    class Meta(TypedModelMeta):
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
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
