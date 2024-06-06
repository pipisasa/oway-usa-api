from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.purchase import models
from apps.purchase import serializers


class PurchaseList(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 5

        purchases = models.Purchase.objects.all()
        result_page = paginator.paginate_queryset(purchases, request)
        serializer = serializers.PurchaseListSerializer(result_page, many=True)

        modified_data = []

        for purchase in serializer.data:
            modified_purchase = purchase.copy()
            modified_purchase['is_paid'] = purchase['payment_confirmation'] is not None
            modified_purchase['request_status'] = purchase['payment_confirmation'] is not None
            modified_data.append(modified_purchase)

        return paginator.get_paginated_response(modified_data)

