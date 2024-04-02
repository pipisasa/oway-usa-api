from rest_framework import serializers

from apps.purchase import models


class PurchaseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Purchase
        fields = '__all__'
