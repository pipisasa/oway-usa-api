from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from apps.address.models import Address
from apps.address.serializers import AddressListSerializer


class AddressDetailAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = AddressListSerializer

    @swagger_auto_schema(
        operation_summary="Get address",
        responses={
            200:AddressListSerializer()
        }
    )
    def get(self, request, id):
        instance = get_object_or_404(Address, id=id)
        serializer = AddressListSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)