simple_filters = [{
    'field': 'unique_id',
}, {
    'field': 'courier_service',
}, {
    'field': 'warehouse',
},
]

text_search_filters = [{
    'fields': ['tracking_number'],
    'query_params_field': 'tracking_number',
},]