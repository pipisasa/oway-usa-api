from rest_framework import serializers

from apps.purchase import models


class PurchaseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Purchase
        fields = '__all__'
