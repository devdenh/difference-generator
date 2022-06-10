

def is_bool(value):
    bool_list = ['false', 'null', 'true', '0']
    for item in bool_list:
        if value == item:
            return value
    if isinstance(value, int):
        return value
    return f"'{value}'"


def plain_formatter(current_value, list):
    lines = []
    for item in current_value:
        if item.get('type') == 'nested':
            key = (item.get('key'))
            lines.append(plain_formatter(item.get('children'), list + [key]))
        elif item.get('type') == 'added':
            value = is_nested(item, 'value')
            lines.append(f"Property '{'.'.join(list + [item.get('key')])}"
                         f"' was added with value: {value}")
        elif item.get('type') == 'removed':
            lines.append(f"Property '{'.'.join(list + [item.get('key')])}"
                         f"' was removed")
        elif item.get('type') == 'changed':
            value1 = is_nested(item, 'value1')
            value2 = is_nested(item, 'value2')
            lines.append(f"Property '{'.'.join(list + [item.get('key')])}"
                         f"' was updated. From "
                         f"{value1} to {value2}")
    return '\n'.join(lines)


def is_nested(item, key):
    result = is_bool(item.get(key))\
        if not isinstance(item.get(key), dict) else '[complex value]'
    return result
