from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.json import make_json


def format(format_name, tree):
    if format_name == 'stylish':
        result = make_stylish(tree)
    elif format_name == 'plain':
        result = plain_formatter(tree)
    elif format_name == 'json':
        result = make_json(tree)
    else:
        raise ValueError
    return result
