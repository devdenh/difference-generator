import json


def to_str(value):
    bool_list = ['false', 'null', 'true', '0']
    for item in bool_list:
        if value == item:
            return value
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    if isinstance(value, int):
        return value
    return f"'{value}'"


def plain_formatter(node, list):
    children = node.get('children')
    key = node.get('key')
    if node.get('type') == 'root':
        lines = map(lambda child: plain_formatter(child, list), children)
        result = "\n".join(lines)
        return result
    if node['type'] == 'nested':
        lines = filter(
            None, (map(
                lambda child: plain_formatter(child, list + [key]), children)
            )
        )
        result = "\n".join(lines)
        return result
    if node['type'] == 'added':
        value = is_nested(node['value'])
        lines = (f"Property '{'.'.join(list + [key])}' "
                 f"was added with value: {value}")
        result = '\n'.join([lines])
        return result
    if node['type'] == 'removed':
        lines = (f"Property '{'.'.join(list + [key])}' "
                 f"was removed")
        result = "\n".join([lines])
        return result
    if node['type'] == 'changed':
        value1 = is_nested(node['value1'])
        value2 = is_nested(node['value2'])
        lines = (f"Property '{'.'.join(list + [key])}' "
                 f"was updated. From {value1} to {value2}")
        result = "\n".join([lines])
        return result


def is_nested(item):
    return '[complex value]' if isinstance(item, dict) else to_str(item)


def make_plain(tree):
    return plain_formatter(tree, [])
