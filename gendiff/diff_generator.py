import os
from gendiff.parser import parser
from gendiff.inner_mapping import make_tree
from gendiff.formatter import format


def generate_diff(file_path1, file_path2, format_name='stylish'):
    paths = (file_path1, file_path2)
    abs_paths = tuple(map(os.path.abspath, paths))
    formated_data = parser(abs_paths)
    tree = make_tree(formated_data[0], formated_data[1])
    result = format(format_name, tree)
    return result
