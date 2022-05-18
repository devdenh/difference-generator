import json
import yaml


def parser(data, type):
    if type == 'json':
        data = json.load(data)
    elif type == 'yaml':
        data = yaml.safe_load(data)
    return data
