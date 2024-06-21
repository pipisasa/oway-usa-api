from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView

from apps.items.models import Item
from apps.items.serializers import ItemListSerializer

from .filter_helpers import text_search_filters


class ItemListAPI(ListAPIView):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        return ItemListSerializer

    def get_queryset(self):
        return Item.objects.all()

    def _filter_queryset(self, request, queryset):
        query_params = request.query_params.copy()

        q_objects = self.build_filters(
            query_params=query_params,
            simple_filters=[],
            in_filters=[],
            boolean_filters=[],
            range_filters=[],
            text_search_filters=text_search_filters,
        )
        queryset = queryset.filter(q_objects)
        return queryset

    @swagger_auto_schema(
        operation_summary="List Items",
        responses={
            200:ItemListSerializer(many=True)
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