from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView
from apps.warehouses.models import Warehouse
from apps.warehouses.serializers import WarehouseListSerializer


class MyWarehouseListAPI(ListAPIView):
    permission_classes = [IsAdminUser]

    def get_unique_id_user(self):
        user_unique_id = self.request.user.unique_id
        return user_unique_id

    def get_serializer_class(self):
        return WarehouseListSerializer

    def get_queryset(self):
        return Warehouse.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)