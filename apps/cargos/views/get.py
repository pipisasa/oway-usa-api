from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.cargos.models import Cargo
from apps.cargos.serializers import CargoSerializer


class CargoGetAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_summary="Get list of cargos",
        responses={200: CargoSerializer()}
    )
    def get(self, request, id):
        cargo = Cargo.objects.filter(id=id).first()
        if not cargo:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CargoSerializer(cargo)
        return Response(serializer.data, status=status.HTTP_200_OK)