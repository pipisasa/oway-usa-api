from rest_framework import serializers

from apps.warehouses.models import StatusPayment


class StatusPaymentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusPayment
        fields = '__all__'


class StatusPaymentDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusPayment
        fields = '__all__'