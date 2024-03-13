from rest_framework import pagination
from .pagination import Pagination


class CursorPagination(Pagination, pagination.CursorPagination):
    pass