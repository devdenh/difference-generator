import json
import yaml


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def parser(paths):
    data_list = []
    for path in paths:
        if path.endswith('json'):
            data = recursive_parser(json.loads(read(path)))
            data_list.append(data)
        else:
            data = yaml.load(read(path), Loader=yaml.BaseLoader)
            data_list.append(data)
    return data_list


def recursive_parser(data):
    for item in data:
        if isinstance(data[item], bool) or data.get(item) is None:
            data[item] = json.dumps(data[item])
        elif isinstance(data[item], dict):
            recursive_parser(data[item])
    return data
