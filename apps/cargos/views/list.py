from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.cargos.models import Cargo
from apps.cargos.serializers import CargoSerializer


class CargoListAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_summary="Get list of cargos",
        responses={200: CargoSerializer(many=True)}
    )
    def get(self, request, format=None):
        cargos = Cargo.objects.all()
        serializer = CargoSerializer(cargos, many=True)
        return Response(serializer.data)