from rest_framework import serializers

from apps.warehouses.models import WarehouseProduct
from .status_serializer import StatusDetailSerializer
from apps.countries.serializers import DetailCountrySerializer
from .status_payment_serializer import StatusPaymentDetailSerializer


class WarehouseProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = WarehouseProduct
        fields = '__all__'


class WarehouseProductListSerializer(serializers.ModelSerializer):
    status = StatusDetailSerializer()
    status_payment = StatusPaymentDetailSerializer()
    country_of_origin = DetailCountrySerializer()
    country_of_destination = DetailCountrySerializer()

    class Meta:
        model = WarehouseProduct
        fields = '__all__'
