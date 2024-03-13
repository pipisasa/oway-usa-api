class Pagination:
    ordering = '-id'
    page_size = 10

    def get_ordering(self, request, queryset, view):
        ordering = request.query_params.get('ordering', self.ordering)
        if not ordering:
            ordering = self.ordering
        return [ordering]

    def get_page_size(self, request):
        return int(request.query_params.get('page_size', self.page_size))
