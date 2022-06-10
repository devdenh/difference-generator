

def make_tree(data1, data2):
    result = []
    for key in sorted(data1.keys() | data2.keys()):
        if all((isinstance(data1.get(key), dict),
                isinstance(data2.get(key), dict))):
            node = {'key': key, 'type': 'nested',
                    'children': make_tree(data1[key], data2[key])}
            result.append(node)
        elif key in data1 and key not in data2:
            node = {'key': key,
                    'type': 'removed',
                    'value': data1.get(key)}
            result.append(node)
        elif key in data2 and key not in data1:
            node = {'key': key,
                    'type': 'added',
                    'value': data2.get(key)}
            result.append(node)
        elif data1.get(key) == data2.get(key):
            node = {'key': key, 'type': 'unchanged',
                    'value': data1.get(key)}
            result.append(node)
        else:
            node = {'key': key, 'type': 'changed',
                    'value1': data1.get(key),
                    'value2': data2.get(key)}
            result.append(node)

    return result
