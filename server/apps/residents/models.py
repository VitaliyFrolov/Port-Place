from django.db import models
from django.utils.translation import gettext_lazy as _
from django_stubs_ext.db.models import TypedModelMeta


class Resident(models.Model):
    title: "models.CharField[str, str]" = models.CharField(verbose_name=_("Company title"), max_length=100)
    description: "models.CharField[str, str]" = models.CharField(verbose_name=_("Company description"), max_length=150)
    resident_phone: "models.CharField[str, str]" = models.CharField(verbose_name=_("Resident phone"), max_length=20)
    photo: "models.ImageField" = models.ImageField(verbose_name=_("Photo"))

    class Meta(TypedModelMeta):
        verbose_name = _("Resident")
        verbose_name_plural = _("Residents")

    def __str__(self) -> str:
        return f"{self.title} -- {self.resident_phone}"
