from django.db import models
from django.utils.translation import gettext_lazy as _


class TableType(models.IntegerChoices):
    billiard = 1, _("Billiard")
    tennis = 2, _("Tennis")

    __empty__ = _("Not defined")
