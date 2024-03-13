
def build_range_filters(
    filters,
    filter_params,
    query_params,
    convert_filter=None,
):
    filter_name = filter_params.get('field')
    query_field = filter_params.get('query_params_field', filter_name)
    query_min_value = query_params.get(f'min_{query_field}')
    query_max_value = query_params.get(f'max_{query_field}')

    key_filter_max = f"{filter_name}__lte"
    key_filter_min = f"{filter_name}__gte"

    filter_value = {}

    if convert_filter:
        if query_max_value:
            filter_value[key_filter_max] = convert_filter(
                filter_name=key_filter_max,
                value=query_max_value,
                value_type=filter_params.get('type'),
            )[key_filter_max]
        if query_min_value:
            filter_value[key_filter_min] = convert_filter(
                filter_name=key_filter_min,
                value=query_min_value,
                value_type=filter_params.get('type'),
            )[key_filter_min]
    else:
        if query_max_value:
            filter_value[key_filter_max] = query_max_value
        if query_min_value:
            filter_value[key_filter_min] = query_min_value

    return {**filters, **filter_value}