from rest_framework import generics, permissions

from apps.my_warehouse.models import MyWarehouse
from apps.my_warehouse.serializers import MyWarehouseCreateUpdateSerializer


class MyWarehouseUpdate(generics.UpdateAPIView):
    queryset = MyWarehouse.objects.all()
    serializer_class = MyWarehouseCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
