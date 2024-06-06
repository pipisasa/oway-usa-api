from rest_framework import serializers

from apps.cities.models import City

base_field = [
    'name',
]


class BaseCitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = base_field


class ListCitySerializer(BaseCitySerializer):

    class Meta:
        model = City
        fields = ["id"] + base_field
