from django.db import models


class GamingTables(models.Model):
    class Meta:
        verbose_name = "Стол"
        verbose_name_plural = "Столы"

    TYPE_OF_GAME = {"pin": "pinpong", "bil": "billiard"}

    game = models.CharField(verbose_name="Вид игры")
