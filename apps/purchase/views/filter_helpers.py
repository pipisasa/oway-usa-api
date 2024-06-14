simple_filters = [{
    'field': 'price',
}, {
    'field': 'created_at',
}, {
    'field': 'warehouse_id',
    'query_params_field': 'warehouse',
}
]

text_search_filters = [{
    'fields': ['name_of_purchase'],
    'query_params_field': 'name_of_purchase',
},]