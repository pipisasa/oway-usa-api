from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView
from apps.warehouses.models import Warehouse
from apps.warehouses.serializers import WarehouseListSerializer


class WarehouseListAPI(ListAPIView):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        return WarehouseListSerializer

    def get_queryset(self):
        return Warehouse.objects.all()

    @swagger_auto_schema(
        operation_summary="List Warehouse",
        responses={
            200:WarehouseListSerializer(many=True)
        }
    )
    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)