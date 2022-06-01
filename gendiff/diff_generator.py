import os
from gendiff.parser import parser
from gendiff.flat_formatter import format_flat
from gendiff.stylish import make_stylish
from gendiff.inner_mapping import make_tree
from gendiff.plain_formatter import plain_formatter
from gendiff.json_formatter import make_json


def generate_diff_(file_path1, file_path2, format_name=None):
    paths = (file_path1, file_path2)
    abs_paths = tuple(map(os.path.abspath, paths))
    formated_data = parser(abs_paths)
    if format_name == 'plain':
        result = plain_formatter(make_tree(formated_data[0], formated_data[1]))
    elif format_name == 'json':
        result = make_json(make_tree(formated_data[0], formated_data[1]))
    elif all(not isinstance(i.get(x), dict) for i in formated_data for x in i):
        result = format_flat(formated_data[0], formated_data[1])
    else:
        result = make_stylish(make_tree(formated_data[0], formated_data[1]))
    return result
