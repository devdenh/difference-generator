import itertools


def build_indent(depth):
    return ' ' * (depth * 4 - 2)


def stringify(data, depth):
    if not isinstance(data, dict):
        if isinstance(data, bool):
            return 'true' if data else 'false'

        if data is None:
            return 'null'

        return str(data)
    indent = build_indent(depth)
    start_ident = build_indent(depth + 1)
    lines = []
    for key, val in data.items():
        lines.append(f'{start_ident + "  "}{key}: '
                     f'{stringify(val, depth + 1)}')
    result = itertools.chain("{", lines, [indent + "  " + "}"])
    return '\n'.join(result)


def iter_(node, depth=0):  # noqa 901
    children = node.get('children')
    indent = build_indent(depth)
    formatted_value = stringify(node.get('value'), depth)
    formatted_value1 = stringify(node.get('value1'), depth)
    formatted_value2 = stringify(node.get('value2'), depth)
    sighns = {'added': '+ ',
              'removed': '- ',
              'unchanged': '  '}
    if node['type'] == 'root':
        lines = map(lambda child: iter_(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'
    if node['type'] == 'nested':
        lines = map(lambda child: iter_(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{indent + "  "}{node["key"]}: ' \
               f'{{\n{result}\n{indent + "  "}}}'
    if node['type'] == 'changed':
        lines = [
            f'{indent + "- "}{node["key"]}: '
            f'{formatted_value1}',
            f'{indent + "+ "}{node["key"]}: '
            f'{formatted_value2}'
        ]
        result = '\n'.join(lines)
        return result
    if node['type'] == 'added':
        lines = [
            f'{indent + sighns.get(node.get("type"))}{node["key"]}: '
            f'{formatted_value}'
        ]
        result = '\n'.join(lines)
        return result
    if node['type'] == 'removed':
        lines = [
            f'{indent + sighns.get(node.get("type"))}{node["key"]}: '
            f'{formatted_value}'
        ]
        result = '\n'.join(lines)
        return result
    if node['type'] == 'unchanged':
        lines = [
            f'{indent + sighns.get(node.get("type"))}{node["key"]}: '
            f'{formatted_value}'
        ]
        result = '\n'.join(lines)
        return result
    raise ValueError("Unknown node type")


def make_stylish(tree):
    return iter_(tree, 0)
