from rest_framework import serializers

from apps.my_warehouse.models import MyWarehouse
from apps.users.serializers import ProfileSerializer


class MyWarehouseListForAdminSerializer(serializers.ModelSerializer):
    user = ProfileSerializer()

    class Meta:
        model = MyWarehouse
        fields = ["id", "warehouse", "tracking_number", "courier_service", "user"]
