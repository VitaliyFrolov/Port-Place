from django.db import models


class ResidentStatuses(models.IntegerChoices):
    in_process = 0, "Заявка на рассмотрении"
    approved = 1, "Активный резидент"
    refused = 2, "Заявка отклонена"
