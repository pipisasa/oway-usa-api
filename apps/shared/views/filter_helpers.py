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


class FilterHelper():

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
