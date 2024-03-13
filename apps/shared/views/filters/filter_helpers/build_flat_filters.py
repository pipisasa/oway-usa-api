
# build '=' and 'in' filters
def build_flat_filters(
    filters,
    filter_params,
    query_params,
    convert_filter=None,
):
    filter_name = filter_params.get('field')
    query_field = filter_params.get('query_params_field', filter_name)
    query_value = query_params.getlist(query_field)
    filter_value = {}
    if len(query_value):
        if convert_filter:
            filter_value = convert_filter(
                filter_name=filter_name,
                value=query_value,
                value_type=filter_params.get('type'),
            )
        else:
            filter_value = {filter_name: query_value}

    return {**filters, **filter_value}