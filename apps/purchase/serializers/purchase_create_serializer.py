from rest_framework import serializers

from apps.purchase.models import Purchase


class PurchaseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        exclude = ['payment_confirmation', 'price']
