from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouses.serializers import WarehouseCreateSerializer
from apps.warehouses.models import WarehouseProduct


class UpdatesWarehouseProductAPI(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Updates Warehouse",
        responses={
            200: "Successfully update",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def patch(self, request, *args, **kwargs):
        ids = request.data.get("ids", [])
        WarehouseProduct.objects.filter(pk__in=ids).update(
            status=request.data.get("status")
        )
        return Response("ok", status=status.HTTP_400_BAD_REQUEST)