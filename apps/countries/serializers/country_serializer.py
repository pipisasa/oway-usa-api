from rest_framework import serializers

from apps.countries.models import Country

base_field = [
    'name',
    'codename',
    'icon'
]


class BaseCountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = base_field


class ListCountrySerializer(BaseCountrySerializer):

    class Meta:
        model = Country
        fields = ["id"] + base_field


class DetailCountrySerializer(BaseCountrySerializer):

    class Meta:
        model = Country
        fields = ["id"] + base_field


class UpdateCountrySerializer(BaseCountrySerializer):

    class Meta:
        model = Country
        fields = ["id"] + base_field
