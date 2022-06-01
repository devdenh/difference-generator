from gendiff.diff_generator import generate_diff_


def generate_diff(path1, path2, format_name=None):
    return generate_diff_(path1, path2, format_name)
