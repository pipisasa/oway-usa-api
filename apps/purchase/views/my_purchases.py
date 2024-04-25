from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView
from apps.purchase.models import Purchase
from apps.purchase.serializers import MyPurchaseListSerializer


class MyPurchasesListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return MyPurchaseListSerializer

    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(user=user)

    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)
