from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView
from apps.clients_outside_of_illinois import serializers, model

from rest_framework import permissions, status

from .filter_helpers import simple_filters, text_search_filters


class ClientsOutsideOfIllinoisListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        return serializers.ClientSerializer

    def get_queryset(self):
        return model.OutsideOfIllinois.objects.all()

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

    def get(self, request):
        queryset = self.get_queryset()
        filtered_queryset = self._filter_queryset(request, queryset)
        base_response, _ = self.get_base_response(filtered_queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)
