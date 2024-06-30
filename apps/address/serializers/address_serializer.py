from rest_framework import serializers

from apps.address.models import Address


class AddressCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class AddressListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'
