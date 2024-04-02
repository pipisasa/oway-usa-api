from rest_framework import serializers

from apps.billing import models


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Billing
        fields = ['id', 'full_name', 'number', 'end_date', 'cvv']
