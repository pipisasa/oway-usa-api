from rest_framework import generics
from rest_framework.permissions import AllowAny

from apps.purchase import models
from apps.purchase import serializers


class CreatePurchase(generics.CreateAPIView):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseCreateSerializer
    permission_classes = [AllowAny]
