from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.warehouses.models import StatusPayment
from apps.warehouses.serializers import StatusPaymentListSerializer


class ListStatusPaymentAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = StatusPaymentListSerializer
    queryset = StatusPayment.objects.all()