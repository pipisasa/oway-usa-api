from rest_framework import serializers

from apps.warehouses.models import Warehouse
from .status_serializer import StatusDetailSerializer
from apps.countries.serializers import DetailCountrySerializer
from .status_payment_serializer import StatusPaymentDetailSerializer


class WarehouseCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Warehouse
        fields = '__all__'


class WarehouseListSerializer(serializers.ModelSerializer):
    country = DetailCountrySerializer()

    class Meta:
        model = Warehouse
        fields = '__all__'
