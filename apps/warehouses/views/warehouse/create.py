from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notifications.models.notifications.mail_box import MailBox
from apps.notifications.models.notifications.notifications import Notifications
from apps.notifications.serializers.notification_serializer import NotificationsSerializer
from apps.users.models import User
from apps.warehouses.models import Warehouse
from apps.warehouses.serializers import WarehouseCreateSerializer


class CreateWarehouseAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = WarehouseCreateSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.filter(unique_id=serializer.validated_data.get('unique_id_user', '')).first()
            if user is not None:
                notification = Notifications(
                        title='Добавлен товар',
                        description='Проверте ваш склад'
                )
                notification.save()
                MailBox.objects.create(user=user, notification=notification)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)