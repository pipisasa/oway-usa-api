from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.address.models import Address
from apps.address.serializers import AddressCreateSerializer


class CreateAddressAPI(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AddressCreateSerializer

    @swagger_auto_schema(
        operation_summary="Create Address",
        request_body=AddressCreateSerializer,
        responses={
            201: "Successfully created",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        if data.get('user', None) is None:
            data['user'] = request.user.id
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
