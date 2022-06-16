import json
import yaml


def parse(data, format_name):
    if format_name == 'json':
        return recursive_parse(json.loads(data))
    elif format_name in {'yml', 'yaml'}:
        return yaml.load(data, Loader=yaml.BaseLoader)
    else:
        raise ValueError('Unknown format')


def recursive_parse(data):
    for item in data:
        if isinstance(data[item], bool) or data.get(item) is None:
            data[item] = json.dumps(data[item])
        elif isinstance(data[item], dict):
            recursive_parse(data[item])
    return data
