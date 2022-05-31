

def is_bool(string):
    bool_list = ['false', 'null', 'true']
    for item in bool_list:
        if string == item:
            return string
    return f"'{string}'"


def plain_formatter(value):

    def iter_(current_value, some_list):
        lines = []
        for item in current_value:
            if item.get('type') == 'nested':
                key = (item.get('key'))
                lines.append(iter_(item.get('children'), some_list + [key]))
            elif item.get('type') == 'added':
                value = is_bool(item.get('value')) if not isinstance(item.get('value'), dict) else '[complex value]'
                lines.append(f"Property '{'.'.join(some_list + [item.get('key')])}' was added with value: {value}")
            elif item.get('type') == 'removed':
                lines.append(f"Property '{'.'.join(some_list + [item.get('key')])}' was removed")
            elif item.get('type') == 'changed':
                value1 = is_bool(item.get('value1')) if not isinstance(item.get('value1'), dict) else '[complex value]'
                value2 = is_bool(item.get('value2')) if not isinstance(item.get('value2'), dict) else '[complex value]'
                lines.append(f"Property '{'.'.join(some_list + [item.get('key')])}' was updated. From "
                             f"{value1} to {value2}")

        return '\n'.join(lines)
    return iter_(value, [])
