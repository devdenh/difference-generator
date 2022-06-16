import os
from gendiff.parser import parse
from gendiff.tree import build
from gendiff.formatter import format


def generate_diff(file_path1, file_path2, format_name='stylish'):
    paths = (file_path1, file_path2)
    abs_paths = tuple(map(os.path.abspath, paths))
    data1, data2 = get_data(abs_paths[0]), get_data(abs_paths[1])
    formated_data1 = parse(data1, get_format(paths[0]))
    formated_data2 = parse(data2, get_format(paths[1]))
    tree = build(formated_data1, formated_data2).get('children')
    result = format(format_name, tree)
    return result


def get_data(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def get_format(path):
    return path.split('.')[1]
