from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.address.models import Address


class DeleteAddressAPI(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Delete Address",
        responses={
            204: "Item successfully deleted",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def delete(self, request, id, *args, **kwargs):
        instance = get_object_or_404(Address, pk=id, user_id=request.user.id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)