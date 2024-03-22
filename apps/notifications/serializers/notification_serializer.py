from rest_framework import serializers

from apps.notifications.models.notifications.notifications import Notifications


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['id', 'title', 'description', 'icon']
