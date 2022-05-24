import hexlet.fs as fs
from gendiff.parser import parser


def make_tree(data1, data2):
    tree = fs.mkdir('/', [])
    def walk(node, data1, data2):
        for key in sorted(data1.keys() & data2.keys()):
            if all((isinstance(data1[key], dict), isinstance(data2[key], dict))):
                children = fs.mkdir(key, [
                    data1[key],
                    data2[key]
                ])
                node['children'].append(children)
                walk(children, data1[key], data2[key])

        return node
    return walk(tree, data1, data2)

from gendiff.parser import data1, data2

print(make_tree(data1, data2))
