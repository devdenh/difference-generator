import json
import os
from gendiff.parser import args

path1 = args.first_file
path2 = args.second_file


def generate_diff_(file_path1, file_path2):
    file_path1 = os.path.abspath(file_path1)
    file_path2 = os.path.abspath(file_path2)

    with open(file_path1) as file1, open(file_path2) as file2:
        data1, data2 = json.load(file1), json.load(file2)

        for item in data1:
            if isinstance(data1[item], bool):
                data1[item] = json.dumps(data1[item])

        for _item in data2:
            if isinstance(data2[_item], bool):
                data2[_item] = json.dumps(data2[_item])

        both_keys = data1.keys() | data2.keys()
        start = '{'
        end = '}'
        print(start)
        for key in sorted(both_keys):
            if key in data1 and key in data2:
                if data1[key] == data2[key]:
                    print(f'    {key}: {data1[key]}')
                else:
                    print(f'  - {key}: {data1[key]}')
                    print(f'  + {key}: {data2[key]}')
            elif key in data1 and key not in data2:
                print(f'  - {key}: {data1[key]}')
            elif key in data2 and key not in data1:
                print(f'  + {key}: {data2[key]}')
        print(end)
