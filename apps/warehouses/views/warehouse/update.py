from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouses.serializers import WarehouseCreateSerializer
from apps.warehouses.models import Warehouse


class UpdateWarehouseAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = WarehouseCreateSerializer

    @swagger_auto_schema(
        operation_summary="Update Warehouse",
        request_body=WarehouseCreateSerializer,
        responses={
            201: "Successfully updated Warehouse",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def put(self, request, pk, *args, **kwargs):
        warehouse_instance = get_object_or_404(Warehouse, pk=pk)
        data = request.data
        serializer = self.serializer_class(warehouse_instance, data=data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update Warehouse",
        request_body=WarehouseCreateSerializer,
        responses={
            201: "Successfully created",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def patch(self, request, pk, *args, **kwargs):
        warehouse_instance = get_object_or_404(Warehouse, pk=pk)
        data = request.data
        serializer = self.serializer_class(warehouse_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)