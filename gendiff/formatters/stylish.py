import itertools
import json


def build_indent(depth):
    return ' ' * (depth * 4 - 2)


def stringify(data, start_depth=1):
    def walk(inner_data, depth):

        if not isinstance(inner_data, dict):
            if isinstance(inner_data, bool) or inner_data is None:
                return json.dumps(inner_data)
            return str(inner_data)
        spaces_count = 4
        deep_indent_size = depth + spaces_count
        deep_indent = ' ' * deep_indent_size
        current_indent = ' ' * depth
        lines = []
        for key, val in inner_data.items():
            lines.append(f'{deep_indent}{key}: '
                         f'{walk(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return f'\n{start_depth * spaces_count * " "}'.join(result)
    return walk(data, 0)


def iter_(node, depth=0):
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
        return f'{indent + "  "}{node["key"]}: '\
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
    else:
        lines = [
            f'{indent + sighns.get(node.get("type"))}{node["key"]}: '
            f'{formatted_value}'
        ]
        result = '\n'.join(lines)
        return result


def make_stylish(tree):
    return iter_(tree, 0)
