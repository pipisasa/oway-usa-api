from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.my_warehouse.models import MyWarehouse
from apps.my_warehouse.serializers import MyWarehouseCreateUpdateSerializer
from apps.shared.views.list_view import ListAPIView


class MyWarehouseListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return MyWarehouseCreateUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return MyWarehouse.objects.filter(user=user)

    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)
