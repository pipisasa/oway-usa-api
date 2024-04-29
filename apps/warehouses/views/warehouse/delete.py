from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notifications.models.notifications.mail_box import MailBox
from apps.notifications.models.notifications.notifications import Notifications
from apps.users.models import User
from apps.warehouses.serializers import WarehouseCreateSerializer
from apps.warehouses.models import Status, Warehouse


class DeleteWarehouseAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = WarehouseCreateSerializer

    def delete(self, request, id, *args, **kwargs):
        warehouse_instance = get_object_or_404(Warehouse, pk=id)
        warehouse_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)