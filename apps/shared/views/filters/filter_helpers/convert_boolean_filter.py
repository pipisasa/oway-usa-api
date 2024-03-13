from typing import List

def convert_boolean_filter(
    filter_name: str,
    value: List[str],
    value_type: str,
):
    real_value = value[0]
    if real_value.lower() == 'true':
        return {filter_name: True}
    if real_value.lower() == 'false':
        return {filter_name: False}
    return {}