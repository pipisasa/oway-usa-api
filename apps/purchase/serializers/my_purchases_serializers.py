from rest_framework import serializers

from apps.purchase.models import Purchase


class MyPurchaseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
