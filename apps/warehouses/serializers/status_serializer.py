from rest_framework import serializers

from apps.warehouses.models import Status


class StatusListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'


class StatusDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = '__all__'