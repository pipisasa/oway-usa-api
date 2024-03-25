from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.billing.models import Billing
from apps.billing.serializers import BillingSerializer


class MyBillingsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        billings = Billing.objects.filter(user=user)
        serializer = BillingSerializer(billings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
