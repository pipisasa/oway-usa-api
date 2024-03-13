from rest_framework import pagination
from django.core.exceptions import FieldError
from .pagination import Pagination


class PageNumberPagination(Pagination, pagination.PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        ordering = self.get_ordering(request, queryset, view)
        try:
            queryset = queryset.order_by(*ordering)
        except FieldError:
            pass
        return super().paginate_queryset(queryset, request, view)
