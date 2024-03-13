
def convert_in_filter(filter_name, value, value_type=None):
    real_value = []
    for item in value:
        if item != '':
            real_value.append(int(item) if value_type == 'int' else item)
    return {f'{filter_name}__in': real_value}