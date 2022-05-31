import os
from gendiff.parser import parser
from gendiff.flat_formatter import format_flat
from gendiff.nested_formatter import stylish
from gendiff.inner_mapping import make_tree
from gendiff.plain_formatter import plain_formatter


def generate_diff_(file_path1, file_path2, format_name=None):
    paths = (file_path1, file_path2)
    abs_paths = tuple(map(os.path.abspath, paths))
    formated_data = parser(abs_paths)
    if any(isinstance(i.get(x), dict) for i in formated_data for x in i)\
            and format_name != 'plain':
        result = stylish(make_tree(formated_data[0], formated_data[1]))
    elif format_name == 'plain':
        result = plain_formatter(make_tree(formated_data[0], formated_data[1]))
    else:
        result = format_flat(formated_data[0], formated_data[1])
    return result
