from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.catalog_sites.models import CatalogSite
from apps.catalog_sites.serializers import CatalogSiteListSerializer
from apps.catalog_sites.views.filter_helpers import simple_filters
from apps.shared.views.list_view import ListAPIView


class ListCatalogSitesAPI(ListAPIView):
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CatalogSite.objects.all()

    def get_serializer_class(self):
        return CatalogSiteListSerializer

    def _filter_queryset(self, request, queryset):
        query_params = request.query_params.copy()

        q_objects = self.build_filters(
            query_params=query_params,
            simple_filters=simple_filters,
            in_filters=[],
            boolean_filters=[],
            range_filters=[],
            text_search_filters=[],
        )
        queryset = queryset.filter(q_objects)
        return queryset

    @swagger_auto_schema(
        responses={200: openapi.Response(
            'List of category sites', CatalogSiteListSerializer(many=True))},
    )
    def get(self, request):
        queryset = self.get_queryset()
        filtered_queryset = self._filter_queryset(request, queryset)
        base_response, _ = self.get_base_response(filtered_queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)