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


class UpdateWarehouseAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = WarehouseCreateSerializer

    def put(self, request, pk, *args, **kwargs):
        warehouse_instance = get_object_or_404(Warehouse, pk=pk)
        data = request.data
        serializer = self.serializer_class(warehouse_instance, data=data, partial=False)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(unique_id=serializer.validated_data.get('unique_id_user', '')).first()
            if user is not None:
                data_status = Status.objects.get(id=data['status'])
                if data_status.name == 'Доставлено':
                    notification = Notifications(
                        title='Товар Доставлен',
                        description='Проверьте ваш склад'
                    )
                    notification.save()
                    MailBox.objects.create(user=user, notification=notification)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        warehouse_instance = get_object_or_404(Warehouse, pk=pk)
        data = request.data
        serializer = self.serializer_class(warehouse_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(unique_id=serializer.validated_data.get('unique_id_user', '')).first()
            if user is not None:
                data_status = Status.objects.get(id=data['status'])
                if data_status.name == 'Доставлено':
                    notification = Notifications(
                        title='Товар Доставлен',
                        description='Проверьте ваш склад'
                    )
                    notification.save()
                    MailBox.objects.create(user=user, notification=notification)
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)