from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.notifications.models.notifications.mail_box import MailBox
from apps.notifications.serializers.notification_serializer import NotificationsSerializer
from apps.users.models import User


class CreateNotificationAPIView(APIView):
    serializer_class = NotificationsSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, format=None):
        serializer = NotificationsSerializer(data=request.data)
        if serializer.is_valid():
            notification = serializer.save()

            users = User.objects.all()
            for user in users:
                MailBox.objects.create(user=user, notification=notification)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
