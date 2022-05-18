import json
import yaml


def parser(data, type):
    if type == 'json':
        data = json.load(data)
        for item in data:
            if isinstance(data[item], bool):
                data[item] = json.dumps(data[item])
    elif type == 'yaml':
        data = yaml.load(data, Loader=yaml.BaseLoader)
    return data
