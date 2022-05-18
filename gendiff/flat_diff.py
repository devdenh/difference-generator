import json
import os
from gendiff.parser import parser


def generate_diff_(file_path1, file_path2):

    paths = (file_path1, file_path2)
    abs_paths = tuple(map(os.path.abspath, paths))
    with open(abs_paths[0]) as file1, open(abs_paths[1]) as file2:
        data_list = []
        for path in abs_paths:
            file_type = 'json' if path.endswith('json') else 'yaml'
            data_list.append(file_type)
        data_tuple = (tuple(map(lambda x, y: (x, y),
                                (file1, file2), data_list)))
        formated_data = []
        for item, type in data_tuple:
            data = parser(item, type)
            formated_data.append(data)
    return flat_differ(formated_data[0], formated_data[1])


def flat_differ(data1, data2):  # noqa: C901

    for item in data1:
        if isinstance(data1[item], bool):
            data1[item] = json.dumps(data1[item])

    for _item in data2:
        if isinstance(data2[_item], bool):
            data2[_item] = json.dumps(data2[_item])

    result = '{\n'
    for key in sorted(data1.keys() | data2.keys()):
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result += f'    {key}: {data1[key]}\n'
            else:
                result += f'  - {key}: {data1[key]}\n'
                result += f'  + {key}: {data2[key]}\n'
        elif key in data1 and key not in data2:
            result += f'  - {key}: {data1[key]}\n'
        elif key in data2 and key not in data1:
            result += f'  + {key}: {data2[key]}\n'
    result += '}'
    return result


# print(generate_diff_('/home/devden/python-project-lvl2/tests/fixtures/file1.yml',
# '/home/devden/python-project-lvl2/tests/fixtures/file2.yml'))
