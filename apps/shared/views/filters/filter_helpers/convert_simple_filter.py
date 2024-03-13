
def convert_simple_filter(filter_name, value, value_type=None):
    real_value = value[0] if isinstance(value, list) else value
    if real_value == '':
        return {}
    if value_type == 'int':
        real_value = int(real_value)
    return {filter_name: real_value}