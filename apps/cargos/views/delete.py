from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from apps.cargos.models import Cargo


class CargoDeleteAPI(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, id):
        try:
            return Cargo.objects.get(pk=id)
        except Cargo.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Delete cargo by ID",
    )
    def delete(self, request, id):
        cargo = self.get_object(id)
        cargo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
