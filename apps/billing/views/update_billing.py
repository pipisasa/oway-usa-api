from rest_framework import generics

from apps.billing.models import Billing
from apps.billing.serializers import BillingSerializer
from apps.billing import permissions


class UpdateBillingAPIView(generics.UpdateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    permission_classes = [permissions.IsOwner]

