import json
import yaml
from tests.fixtures.expected import read
from tests.fixtures.expected import get_fixture_path
import hexlet.fs as fs


def parser(data, type):
    if type == 'json':
        data = json.loads(data)
        for item in data:
            if isinstance(data[item], bool):
                data[item] = json.dumps(data[item])
            elif isinstance(data[item], dict):
                return recursive_parser(data)
    elif type == 'yaml':
        data = yaml.load(data, Loader=yaml.BaseLoader)
    return data


def recursive_parser(data):
    for item in data:
        if isinstance(data[item], bool):
            data[item] = json.dumps(data[item])
        elif isinstance(data[item], dict):
            recursive_parser(data[item])
    return data


data1 = (parser(read(get_fixture_path('nested_file1.json')), 'json'))
data2 = (yaml.load(read(get_fixture_path('nested_file2.yml')), Loader=yaml.BaseLoader))


# print(data1)
# print(data2)

