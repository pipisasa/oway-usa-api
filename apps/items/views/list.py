from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView

from apps.items.models import Item
from apps.items.serializers import ItemListSerializer


class ItemListAPI(ListAPIView):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return ItemListSerializer

    def get_queryset(self):
        return Item.objects.all()

    @swagger_auto_schema(
        operation_summary="List Items",
        responses={
            200:ItemListSerializer(many=True)
        }
    )
    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)