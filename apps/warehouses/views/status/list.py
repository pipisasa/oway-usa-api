from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.warehouses.models import Status
from apps.warehouses.serializers import StatusListSerializer


class ListStatusAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = StatusListSerializer
    queryset = Status.objects.all()