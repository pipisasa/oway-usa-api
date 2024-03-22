from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.notifications.models.notifications.mail_box import MailBox
from apps.notifications.models.notifications.notifications import Notifications


class DeleteNotificationAPIView(APIView):
    permission_classes = [IsAdminUser]
    def delete(self, request, pk, format=None):
        notification = get_object_or_404(Notifications, pk=pk)
        notification.delete()

        MailBox.objects.filter(notification=notification).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
