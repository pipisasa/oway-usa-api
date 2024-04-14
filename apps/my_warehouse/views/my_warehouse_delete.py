from rest_framework import generics, permissions

from apps.my_warehouse.models import MyWarehouse


class MyWarehouseDelete(generics.DestroyAPIView):
    queryset = MyWarehouse.objects.all()
    permission_classes = [permissions.IsAdminUser]
