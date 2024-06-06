from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from apps.cargos.models import Cargo
from apps.cargos.serializers import CargoSerializer


class CargoUpdateAPI(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = CargoSerializer

    def get_object(self, id):
        try:
            return Cargo.objects.get(pk=id)
        except Cargo.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        operation_summary="Update cargo by ID",
        request_body=CargoSerializer,
        responses={200: CargoSerializer()}
    )
    def put(self, request, id):
        cargo = self.get_object(id)
        serializer = CargoSerializer(cargo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Partially update cargo by ID",
        request_body=CargoSerializer,
        responses={200: CargoSerializer()}
    )
    def patch(self, request, id):
        cargo = self.get_object(id)
        serializer = CargoSerializer(cargo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
