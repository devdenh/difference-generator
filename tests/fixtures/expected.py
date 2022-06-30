import os


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, file_name)


nested_data = read(get_fixture_path('stylish.txt'))
plain_data = read(get_fixture_path('plain.txt'))


def expected_for_nested_diff_json():
    return nested_data
