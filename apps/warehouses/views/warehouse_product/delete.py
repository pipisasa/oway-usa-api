from django.shortcuts import get_object_or_404
from drf_yasg import openapi
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
        operation_description="Delete warehouse products by ID(s). Pass 'all' to delete all warehouse products.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'ids': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_INTEGER),
                    description="List of IDs of the warehouse products to delete"
                )
            }
        ),
        responses={
            204: "Warehouse Product(s) deleted successfully",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def delete(self, request, *args, **kwargs):
        ids = request.data.get('ids', None)

        if ids is None:
            return Response({"detail": "No IDs provided"}, status=status.HTTP_400_BAD_REQUEST)

        if ids == 'all':
            WarehouseProduct.objects.all().delete()
        else:
            if not isinstance(ids, list):
                return Response({"detail": "IDs should be provided as a list"}, status=status.HTTP_400_BAD_REQUEST)

            for id in ids:
                warehouse_product_instance = get_object_or_404(WarehouseProduct, pk=id)
                warehouse_product_instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)