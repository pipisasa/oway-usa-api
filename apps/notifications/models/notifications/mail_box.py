from django.db import models

from apps.notifications.models.notifications.notifications import Notifications
from oway_usa_api import settings


class MailBox(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notifications, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
