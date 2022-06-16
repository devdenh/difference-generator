import itertools


def format_dict(data, sd=1, spaces_count=4):
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
        return f'\n{sd*" "}'.join(result)
        # sd = start_depth
    return walk(data, 0)


def make_stylish(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):

        dis = depth + spaces_count  # deep_ident_size
        di = replacer * dis  # deep_ident
        current_indent = replacer * depth
        sighns = {'added': '+ ',
                  'removed': '- ',
                  'unchanged': '  '}
        lines = []
        for item in current_value:
            if item.get('type') == 'nested':
                lines.append(f'{di}{item.get("key")}: '
                             f'{iter_(item.get("children"), dis)}')
            elif item.get('type') == 'changed':
                lines.append(f'{di[:-2] + "- "}{item.get("key")}: '
                             f'{format_dict(item.get("value1"), sd=dis)}')
                lines.append(f'{di[:-2] + "+ "}{item.get("key")}: '
                             f'{format_dict(item.get("value2"), sd=dis)}')
            else:
                lines.append(f'{di[:-2] + sighns.get(item.get("type"))}'
                             f'{item.get("key")}: '
                             f'{format_dict(item.get("value"), sd=dis)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)
