from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notifications.models.notifications.mail_box import MailBox


class CheckAllNotificationsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        MailBox.objects.filter(user=user).update(status=False)
        return Response(status=status.HTTP_200_OK)
