from rest_framework import serializers

from apps.items.models import Item


class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class ItemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
