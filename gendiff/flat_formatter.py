def format_flat(data1, data2):

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
