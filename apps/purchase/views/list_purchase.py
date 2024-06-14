from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.purchase import models
from apps.purchase import serializers
from apps.shared.views.list_view import ListAPIView

from .filter_helpers import text_search_filters, simple_filters


class PurchaseList(ListAPIView):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        return serializers.PurchaseListSerializer

    def _filter_queryset(self, request, queryset):
        query_params = request.query_params.copy()

        q_objects = self.build_filters(
            query_params=query_params,
            simple_filters=simple_filters,
            in_filters=[],
            boolean_filters=[],
            range_filters=[],
            text_search_filters=text_search_filters,
        )
        queryset = queryset.filter(q_objects)
        return queryset

    def get_queryset(self):
        return models.Purchase.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        filtered_queryset = self._filter_queryset(request, queryset)
        base_response, _ = self.get_base_response(filtered_queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)