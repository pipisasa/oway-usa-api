from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.purchase import models
from apps.purchase import serializers


class PurchaseList(generics.ListAPIView):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseListSerializer
    permission_classes = [IsAdminUser]
