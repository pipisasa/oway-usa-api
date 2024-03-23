from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.notifications.models.notifications.mail_box import MailBox
from apps.notifications.serializers.mail_box_serializer import MailBoxSerializer


class UserNotificationsListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user

        all_notifications = MailBox.objects.filter(user=user)
        all_notifications_serializer = MailBoxSerializer(all_notifications, many=True)

        not_checked_notifications = MailBox.objects.filter(user=user, status=False)
        not_checked_notifications_serializer = MailBoxSerializer(not_checked_notifications, many=True)


        data = {
            'all_notifications': all_notifications_serializer.data,
            'not_checked_notifications': not_checked_notifications_serializer.data,
            'total_notifications': len(all_notifications),
            'total_not_checked_notifications': len(not_checked_notifications)
        }

        return Response(data, status=status.HTTP_200_OK)
