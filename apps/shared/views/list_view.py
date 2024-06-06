from rest_framework.views import APIView
from abc import ABC, abstractmethod
from django.db.models import Q

from .paginations import CursorPagination, PageNumberPagination
from .filters import (
    build_flat_filters,
    build_range_filters,
    build_text_search_filters,
    convert_simple_filter,
    convert_in_filter,
    convert_boolean_filter,
)


class ListAPIView(APIView, ABC):
    @abstractmethod
    def get_queryset(self):
        pass

    @abstractmethod
    def get_serializer_class(self):
        pass

    def build_filters(
            self,
            query_params,
            simple_filters=[],
            in_filters=[],
            boolean_filters=[],
            range_filters=[],
            text_search_filters=[],
    ):
        filters = {}
        for item in simple_filters:
            filters = build_flat_filters(
                filters=filters,
                filter_params=item,
                query_params=query_params,
                convert_filter=convert_simple_filter,
            )
        for item in in_filters:
            filters = build_flat_filters(
                filters=filters,
                filter_params=item,
                query_params=query_params,
                convert_filter=convert_in_filter,
            )
        for item in boolean_filters:
            filters = build_flat_filters(
                filters=filters,
                filter_params=item,
                query_params=query_params,
                convert_filter=convert_boolean_filter,
            )
        for item in range_filters:
            filters = build_range_filters(
                filters=filters,
                filter_params=item,
                query_params=query_params,
                convert_filter=convert_simple_filter,
            )
        q_objects = Q()
        if filters:
            q_objects = Q(**filters)
        for item in text_search_filters:
            q_objects = build_text_search_filters(
                q_objects=q_objects,
                filter_params=item,
                query_params=query_params,
            )
        return q_objects

    def _get_result(self, paginator, queryset, request):
        serializer_class = self.get_serializer_class()
        result_page = paginator.paginate_queryset(queryset, request)
        queryset_serializer = serializer_class(result_page, many=True)
        return queryset_serializer.data

    def get_base_response(self, queryset, request):
        is_page_number_pagination = request.query_params.get(
            'pagination_type'
        ) == 'page_number'

        if is_page_number_pagination:
            paginator = PageNumberPagination()
            results = self._get_result(paginator, queryset, request)
            return {
                'results': results,
                'total_pages': paginator.page.paginator.num_pages,
                'current_page': paginator.page.number,
                'count': queryset.count(),
            }, paginator

        paginator = CursorPagination()
        return {
               'results': self._get_result(paginator, queryset, request),
               'next': paginator.get_next_link(),
               'previous': paginator.get_previous_link(),
               'count': queryset.count(),
           }, paginator

