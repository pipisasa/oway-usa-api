from rest_framework import serializers

from apps.my_warehouse.models import MyWarehouse


class MyWarehouseCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyWarehouse
        fields = ["id", "warehouse", "tracking_number", "courier_service"]
