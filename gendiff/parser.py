import json
import yaml


def parse(data, format_name):
    if format_name == 'json':
        return json.load(data)
    if format_name in {'yml', 'yaml'}:
        return yaml.load(data, Loader=yaml.BaseLoader)
    raise ValueError(f'Unknown format: {format_name}')
