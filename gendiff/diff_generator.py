import os
from gendiff.tree import build
from gendiff.formatter import format
import json
import yaml


def generate_diff(file_path1, file_path2, format_name='stylish'):
    paths = (file_path1, file_path2)
    abs_paths = tuple(map(os.path.abspath, paths))
    data1 = get_data(abs_paths[0], get_format(abs_paths[0]))
    data2 = get_data(abs_paths[1], get_format(abs_paths[1]))
    tree = build(data1, data2)
    return format(format_name, tree)


def get_data(file_path, format_name):
    with open(file_path, 'r') as f:
        if format_name == 'json':
            return json.load(f)
        if format_name in {'yml', 'yaml'}:
            return yaml.load(f, Loader=yaml.BaseLoader)
        raise ValueError(f'Unknown format: {format_name}')


def get_format(path):
    return os.path.splitext(path)[1][1:]
