

def to_str(value):  # noqa  901
    bool_list = ['false', 'null', 'true', '0']
    for item in bool_list:
        if value == item:
            return value
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, int):
        return value
    if isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def plain_formatter(node, ancestry=''):
    children = node.get('children')
    property_name = f"{ancestry}{node.get('key')}"
    if node.get('type') == 'root':
        lines = map(lambda child: plain_formatter(child), children)
        result = "\n".join(lines)
        return result
    if node['type'] == 'nested':
        lines = filter(
            None, (map(
                lambda child: plain_formatter(child, f"{property_name}."),
                children)
            )
        )
        result = "\n".join(lines)
        return result
    if node['type'] == 'added':
        value = to_str(node['value'])
        lines = (f"Property '{property_name}' "
                 f"was added with value: {value}")
        result = '\n'.join([lines])
        return result
    if node['type'] == 'removed':
        lines = (f"Property '{property_name}' "
                 f"was removed")
        result = "\n".join([lines])
        return result
    if node['type'] == 'changed':
        value1 = to_str(node['value1'])
        value2 = to_str(node['value2'])
        lines = (f"Property '{property_name}' "
                 f"was updated. From {value1} to {value2}")
        result = "\n".join([lines])
        return result


def make_plain(tree):
    return plain_formatter(tree)
