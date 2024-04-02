from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from apps.warehouses.models import Warehouse
from apps.warehouses.serializers import WarehouseCreateSerializer


class CreateWarehouseAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = WarehouseCreateSerializer
    queryset = Warehouse.objects.all()