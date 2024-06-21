from drf_yasg.utils import swagger_auto_schema
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

    def get_warehouse(self, id):
        return Warehouse.objects.filter(id=id).first()

    @swagger_auto_schema(
        operation_summary="Get Warehouse",
        responses={
            200: WarehouseListSerializer()
        }
    )
    def get(self, request, id):
        warehouse = self.get_warehouse(id=id)

        if not warehouse:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WarehouseListSerializer(warehouse)

        return Response(serializer.data, status=status.HTTP_200_OK)