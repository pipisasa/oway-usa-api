from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
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

    @swagger_auto_schema(
        operation_summary="Delete Warehouse",
        responses={
            204: "Warehouse successfully deleted",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def delete(self, request, id, *args, **kwargs):
        warehouse_instance = get_object_or_404(Warehouse, pk=id)
        warehouse_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)