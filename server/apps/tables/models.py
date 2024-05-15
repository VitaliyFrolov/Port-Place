from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta

from server.apps.tables.const import TableType


class Table(models.Model):
    number: "models.PositiveSmallIntegerField[int, int]" = models.PositiveSmallIntegerField(
        verbose_name=_("Table number"), primary_key=True
    )
    table_type: "models.PositiveSmallIntegerField[int, int]" = models.PositiveSmallIntegerField(
        verbose_name=_("Table type"), choices=TableType.choices
    )

    class Meta(TypedModelMeta):
        verbose_name = _("Table")
        verbose_name_plural = _("Tables")

    def __str__(self) -> str:
        return f"{self.number} -- {self.table_type}"
