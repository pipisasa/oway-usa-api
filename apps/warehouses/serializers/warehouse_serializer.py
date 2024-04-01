from rest_framework import serializers

from apps.warehouses.models import Warehouse
from .status_serializer import StatusDetailSerializer
from ...countries.serializers import DetailCountrySerializer


class WarehouseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseListSerializer(serializers.ModelSerializer):
    status = StatusDetailSerializer()
    country = DetailCountrySerializer()

    class Meta:
        model = Warehouse
        fields = '__all__'
