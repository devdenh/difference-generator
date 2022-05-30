import itertools


def format_dict(data, start_depth=1, spaces_count=4):
    def walk(inner_data, depth):

        if not isinstance(inner_data, dict):
            return str(inner_data)

        deep_indent_size = depth + spaces_count
        deep_indent = ' ' * deep_indent_size
        current_indent = ' ' * depth
        lines = []
        for key, val in inner_data.items():
            lines.append(f'{deep_indent}{key}: {walk(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return f'\n{start_depth*" "}'.join(result)

    return walk(data, 0)


def stylish(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict) and not isinstance(current_value, list):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for item in current_value:
            if item.get('type') == 'nested':
                lines.append(f'{deep_indent}{item.get("key")}: '
                             f'{iter_(item.get("children"), deep_indent_size)}')
            elif item.get('type') == 'added':
                if not isinstance(item.get('value'), dict):
                    lines.append(f'{deep_indent[:-2] + "+ "}{item.get("key")}: '
                                 f'{format_dict(item.get("value"), start_depth=deep_indent_size)}')
                if isinstance(item.get('value'), dict):
                    lines.append(f'{deep_indent[:-2] + "+ "}{item.get("key")}:'
                                 f' {format_dict(item.get("value"), start_depth=deep_indent_size)}')
            elif item.get('type') == 'unchanged':
                lines.append(f'{deep_indent}{item.get("key")}: {item.get("value")}')
            elif item.get('type') == 'removed':
                if not isinstance(item.get('value'), dict):
                    lines.append(f'{deep_indent[:-2] + "- "}{item.get("key")}: {item.get("value")}')
                if isinstance(item.get('value'), dict):
                    lines.append(f'{deep_indent[:-2] + "- "}{item.get("key")}: '
                                 f'{format_dict(item.get("value"), start_depth=deep_indent_size)}')
            elif item.get('type') == 'changed':
                lines.append(f'{deep_indent[:-2] + "- "}{item.get("key")}: '
                             f'{format_dict(item.get("value1"), start_depth=deep_indent_size)}')
                lines.append(f'{deep_indent[:-2] + "+ "}{item.get("key")}: '
                             f'{format_dict(item.get("value2"), start_depth=deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
