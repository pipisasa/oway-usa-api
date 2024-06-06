from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouses.models import WarehouseProduct
from apps.warehouses.serializers import WarehouseProductListSerializer


class WarehouseProductGetAPI(APIView):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return WarehouseProductListSerializer

    def get_warehouse(self, track_number):
        return WarehouseProduct.objects.filter(track_number=track_number).first()

    def get(self, request, track_number):
        warehouse_product = self.get_warehouse(track_number=track_number)

        if not warehouse_product:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = WarehouseProductListSerializer(warehouse_product)

        return Response(serializer.data, status=status.HTTP_200_OK)