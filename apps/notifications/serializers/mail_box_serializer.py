from rest_framework import serializers

from apps.notifications.models.notifications.mail_box import MailBox
from apps.notifications.serializers.notification_serializer import NotificationsSerializer


class MailBoxSerializer(serializers.ModelSerializer):
    notification = NotificationsSerializer()

    class Meta:
        model = MailBox
        fields = ['id', 'user', 'notification', 'status']
