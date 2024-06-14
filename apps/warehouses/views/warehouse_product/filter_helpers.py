simple_filters = [{
    'field': 'warehouse_id',
    'query_params_field': 'warehouse',
}, {
    'field': 'status_id',
    'query_params_field': 'status',
}, {
    'field': 'status_payment_id',
    'query_params_field': 'status_payment',
}, {
    'field': 'country_of_origin_id',
    'query_params_field': 'country_of_origin',
}, {
    'field': 'country_of_destination_id',
    'query_params_field': 'country_of_destination',
}, {
    'field': 'weight',
}, {
    'field': 'length',
}, {
    'field': 'width',
}, {
    'field': 'height',
}, {
    'field': 'track_number',
}, {
    'field': 'price',
}, {
    'field': 'articul',
}, {
    'field': 'unique_id_user',
}, {
    'field': 'date_sent',
}, {
    'field': 'date_arrived',
},
]

text_search_filters = [{
    'fields': ['name'],
    'query_params_field': 'name',
}, {
    'fields': ['comments'],
    'query_params_field': 'comments',
}]

range_filters = [
    {'field': 'price', 'type': 'int'},
    {'field': 'wage', 'type': 'int'}
]
