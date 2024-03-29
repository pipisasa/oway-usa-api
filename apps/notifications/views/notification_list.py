from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.notifications.models.notifications.notifications import Notifications
from apps.notifications.serializers.notification_serializer import NotificationsSerializer


class NotificationsListAPIView(generics.ListAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
    permission_classes = [IsAdminUser]
