simple_filters = [
    {
        'fields': 'id',
    },
    {
        'field': 'cargo_weight',
    },
]

text_search_filters = [{
    'fields': ['address'],
    'query_params_field': 'address',
}, {
    'fields': ['full_name'],
    'query_params_field': 'full_name',
}, {
    'fields': ['phone_number'],
    'query_params_field': 'phone_number',
}, {
    'fields': ['telegram'],
    'query_params_field': 'telegram',
}, {
    'fields': ['whatsapp'],
    'query_params_field': 'whatsapp',
},
]
