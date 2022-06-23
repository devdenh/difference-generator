from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


def format(format_name, tree):
    if format_name == 'stylish':
        return make_stylish(tree)
    if format_name == 'plain':
        return make_plain(tree)
    if format_name == 'json':
        return make_json(tree)
    raise ValueError(f'Unknown format: {format_name}')
