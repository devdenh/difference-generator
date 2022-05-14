import json
import os


def generate_diff_(file_path1, file_path2):

    with open(os.path.abspath(file_path1)) as file1,\
            open(os.path.abspath(file_path2)) as file2:
        data1, data2 = json.load(file1), json.load(file2)

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
