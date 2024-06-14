from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView
from apps.warehouses.models import WarehouseProduct
from apps.warehouses.serializers import WarehouseProductListSerializer
from .filter_helpers import simple_filters, text_search_filters, range_filters


class WarehouseProductListAPI(ListAPIView):
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        return WarehouseProductListSerializer

    def get_queryset(self):
        return WarehouseProduct.objects.all()

    def _filter_queryset(self, request, queryset):
        query_params = request.query_params.copy()

        q_objects = self.build_filters(
            query_params=query_params,
            simple_filters=simple_filters,
            in_filters=[],
            boolean_filters=[],
            range_filters=range_filters,
            text_search_filters=text_search_filters,
        )
        queryset = queryset.filter(q_objects)
        return queryset

    @swagger_auto_schema(
        operation_summary="List Warehouse Product",
        responses={
            200: WarehouseProductListSerializer(many=True)
        }
    )
    def get(self, request):
        queryset = self.get_queryset()
        filtered_queryset = self._filter_queryset(request, queryset)
        base_response, _ = self.get_base_response(filtered_queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)