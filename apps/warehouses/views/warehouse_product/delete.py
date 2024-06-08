from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouses.models import WarehouseProduct


class DeleteWarehouseProductAPI(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Delete Warehouse Product API",
        operation_description="id: delete a warehouse product\nall: delete all warehouse products",
        responses={
            204: "Warehouse Product deleted successfully",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def delete(self, request, id, *args, **kwargs):

        if id != 'all':
            warehouse_product_instance = get_object_or_404(WarehouseProduct, pk=int(id))
        else:
            warehouse_product_instance = WarehouseProduct.objects.all()

        warehouse_product_instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
