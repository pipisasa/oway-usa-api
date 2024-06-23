from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contacts.serializers import ContactCreateSerializer
from apps.contacts.models import Contact


class UpdateContactAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContactCreateSerializer

    @swagger_auto_schema(
        operation_summary="Update Contact",
        request_body=ContactCreateSerializer,
        responses={
            201: "Successfully updated Contact",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def put(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Contact, pk=pk)
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=False)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Update Contact",
        request_body=ContactCreateSerializer,
        responses={
            201: "Successfully update",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def patch(self, request, pk, *args, **kwargs):
        instance = get_object_or_404(Contact, pk=pk)
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)