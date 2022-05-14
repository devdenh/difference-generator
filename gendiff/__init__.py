from gendiff.flat_diff import generate_diff_
from gendiff.parser import args
path1 = args.first_file
path2 = args.second_file


def generate_diff(path1, path2):
    return generate_diff_(path1, path2)
