from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouses.models import Warehouse
from apps.warehouses.serializers import WarehouseListSerializer


class WarehouseGetAPI(APIView):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return WarehouseListSerializer

    def get_warehouse(self, track_number):
        return Warehouse.objects.filter(track_number=track_number).first()

    def get(self, request, track_number):
        warehouse = self.get_warehouse(track_number=track_number)
        serializer = WarehouseListSerializer(warehouse)

        return Response(serializer.data, status=status.HTTP_200_OK)