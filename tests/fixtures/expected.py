import os


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, file_name)


nested_data = read(get_fixture_path('nested.txt')).rstrip().split('\n\n\n')


def expected_for_flat_diff_json():
    start = '{'
    end = '}'
    return (f'{start}\n  '
                f'- follow: false\n  '
                f'  host: hexlet.io\n  '
                f'- proxy: 123.234.53.22\n  '
                f'- timeout: 50\n  '
                f'+ timeout: 20\n  '
                f'+ verbose: true\n'
                f'{end}')


def expected_for_nested_diff_json():
    return nested_data

