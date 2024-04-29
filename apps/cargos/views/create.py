from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.cargos.serializers import CargoSerializer


class CargoCreateAPI(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CargoSerializer

    @swagger_auto_schema(
        operation_summary="Create a cargo",
        request_body=CargoSerializer,
        responses={201: CargoSerializer()}
    )
    def post(self, request):
        serializer = CargoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)