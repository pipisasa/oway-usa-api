from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.my_warehouse.models import MyWarehouse
from apps.my_warehouse.serializers import MyWarehouseListForAdminSerializer
from apps.shared.views.list_view import ListAPIView


class MyWarehouseForAdminListView(ListAPIView):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        return MyWarehouseListForAdminSerializer

    def get_queryset(self):
        return MyWarehouse.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)
