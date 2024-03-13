
from functools import reduce
from django.db.models import Q


def build_text_search_filters(
    q_objects,
    filter_params,
    query_params,
):
    fields = filter_params.get('fields')
    query_field = filter_params.get('query_params_field', fields[0])
    query_value = query_params.get(query_field)
    if query_value:
        keywords = query_value.split()

        if len(keywords) > 20:
            keywords = keywords[:20]

        for keyword in keywords:
            q_objects &= reduce(lambda acc, field: acc | Q(**{f'{field}__icontains': keyword}), fields, Q())

    return q_objects