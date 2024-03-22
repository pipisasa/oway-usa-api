from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notifications.models.notifications.mail_box import MailBox
from apps.notifications.serializers.mail_box_serializer import MailBoxSerializer


class MailBoxDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get and update MailBox status",
        responses={200: MailBoxSerializer()},
    )
    def get(self, request, pk):
        mailbox = get_object_or_404(MailBox, pk=pk)
        mailbox.status = True
        mailbox.save()
        serializer = MailBoxSerializer(mailbox)
        return Response(serializer.data, status=status.HTTP_200_OK)
