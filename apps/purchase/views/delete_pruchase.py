from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.purchase.models import Purchase


class DeletePurchaseAPI(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Delete Purchase API",
        responses={
            204: "Warehouse Product deleted successfully",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def delete(self, request, id, *args, **kwargs):

        purchase = get_object_or_404(Purchase, id=id)
        purchase.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)