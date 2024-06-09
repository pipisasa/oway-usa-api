from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.items.serializers import ItemCreateSerializer
from apps.items.models import Item


class UpdateItemAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = ItemCreateSerializer

    @swagger_auto_schema(
        operation_summary="Update Warehouse",
        request_body=ItemCreateSerializer,
        responses={
            201: "Successfully updated item",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def put(self, request, pk, *args, **kwargs):
        item_instance = get_object_or_404(Item, pk=pk)
        data = request.data
        serializer = self.serializer_class(item_instance, data=data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update tem",
        request_body=ItemCreateSerializer,
        responses={
            201: "Successfully created",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def patch(self, request, pk, *args, **kwargs):
        item_instance = get_object_or_404(Item, pk=pk)
        data = request.data
        serializer = self.serializer_class(item_instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)