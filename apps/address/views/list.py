from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView

from apps.address.models import Address
from apps.address.serializers import AddressListSerializer


class AddressListAPI(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return AddressListSerializer

    def get_queryset(self):
        return Address.objects.filter(user_id=self.user_id)

    @swagger_auto_schema(
        operation_summary="List Items",
        responses={
            200:AddressListSerializer(many=True)
        }
    )
    def get(self, request):
        self.user_id = request.user.id
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)