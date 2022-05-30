

def make_tree(item1, item2):

    def walk(data1, data2):
        result = []
        for key in sorted(data1.keys() | data2.keys()):
            if all((isinstance(data1.get(key), dict), isinstance(data2.get(key), dict))):
                node = {'key': key, 'type': 'nested', 'children': walk(data1[key], data2[key])}
                result.append(node)
            elif key in data1 and key in data2:
                if data1.get(key) == data2.get(key):
                    node = {'key': key, 'type': 'unchanged', 'value': data1.get(key)}
                    result.append(node)
                else:
                    node = {'key': key, 'type': 'changed', 'value1': data1.get(key), 'value2': data2.get(key)}
                    result.append(node)
            elif key in data1 and key not in data2:
                node = {'key': key, 'type': 'removed', 'value': data1.get(key)}
                result.append(node)
            elif key in data2 and key not in data1:
                node = {'key': key, 'type': 'added', 'value': data2.get(key)}
                result.append(node)
        return result
    return walk(item1, item2)
