from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contacts.models import Contact


class DeleteContactAPI(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Delete Contact",
        responses={
            204: "Contact successfully deleted",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def delete(self, request, id, *args, **kwargs):
        item_instance = get_object_or_404(Contact, pk=id)
        item_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)