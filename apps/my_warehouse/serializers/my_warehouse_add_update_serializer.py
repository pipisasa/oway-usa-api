from rest_framework import serializers

from apps.my_warehouse.models import MyWarehouse


class MyWarehouseCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyWarehouse
        fields = "__all__"
