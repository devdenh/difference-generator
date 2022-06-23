def make_tree(data1, data2):
    result = []
    for key in sorted(data1.keys() | data2.keys()):
        if (
                isinstance(data1.get(key), dict)
                and isinstance(data2.get(key), dict)  # noqa503
        ):
            result.append({
                'key': key,
                'type': 'nested',
                'children': make_tree(data1[key], data2[key])
            })
        elif key in data1 and key not in data2:
            result.append({
                'key': key,
                'type': 'removed',
                'value': data1.get(key)
            })
        elif key in data2 and key not in data1:
            result.append({
                'key': key,
                'type': 'added',
                'value': data2.get(key)
            })
        elif data1.get(key) == data2.get(key):
            result.append({
                'key': key,
                'type': 'unchanged',
                'value': data1.get(key)
            })
        else:
            result.append({
                'key': key,
                'type': 'changed',
                'value1': data1.get(key),
                'value2': data2.get(key)
            })
    return result


def build(data1, data2):
    return {'type': 'root', 'children': make_tree(data1, data2)}
