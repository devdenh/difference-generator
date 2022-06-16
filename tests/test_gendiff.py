from gendiff import generate_diff
import json
from tests.fixtures.expected import expected_for_flat_diff_json
from tests.fixtures.expected import expected_for_nested_diff_json
from tests.fixtures.expected import get_fixture_path
from tests.fixtures.expected import plain_data


# @pytest.fixture(scope='module')
# def file1_json(tmpdir_factory):
#     python_file1_data = {
#         "host": "hexlet.io",
#         "timeout": 50,
#         "proxy": "123.234.53.22",
#         "follow": False
#     }
#
#     file1 = tmpdir_factory.mktemp('data').join('python_file1_data')
#
#     with file1.open('w') as f:
#         json.dump(python_file1_data, f)
#     return file1
#
#
# @pytest.fixture(scope='module')
# def file2_json(tmpdir_factory):
#     python_file2_data = {
#         "timeout": 20,
#         "verbose": True,
#         "host": "hexlet.io"
#     }
#
#     file2 = tmpdir_factory.mktemp('data').join('python_file2_data')
#
#     with file2.open('w') as f:
#         json.dump(python_file2_data, f)
#     return file2
#
#
# @pytest.fixture(scope='module')
# def file1_yml(tmpdir_factory):
#     python_file1_data = {
#         "host": "hexlet.io",
#         "timeout": 50,
#         "proxy": "123.234.53.22",
#         "follow": False
#     }
#
#     file1 = tmpdir_factory.mktemp('data').join('python_file1_data')
#
#     with file1.open('w') as f:
#         yaml.dump(python_file1_data, f)
#     return file1
#
#
# @pytest.fixture(scope='module')
# def file2_yml(tmpdir_factory):
#     python_file2_data = {
#         "timeout": 20,
#         "verbose": True,
#         "host": "hexlet.io"
#     }
#
#     file2 = tmpdir_factory.mktemp('data').join('python_file2_data')
#
#     with file2.open('w') as f:
#         yaml.dump(python_file2_data, f)
#     return file2


def test_flatdiff_json():
    expected = expected_for_flat_diff_json()
    assert generate_diff(get_fixture_path('file1.json'),
                         get_fixture_path('file2.json')) == expected


def test_is_string():
    assert isinstance(generate_diff(get_fixture_path('file1.json'),
                      get_fixture_path('file2.json')), str)


def test_flatdiff_yaml():
    expected = expected_for_flat_diff_json()
    assert generate_diff(get_fixture_path('file1.yml'),
                         get_fixture_path('file2.yml')) == expected


def test_is_string_yml():
    assert isinstance(generate_diff(get_fixture_path('file1.yml'),
                      get_fixture_path('file2.yml')), str)


nested = expected_for_nested_diff_json()


def test_nested_json():
    assert [generate_diff(get_fixture_path('nested_file1.json'),
                          get_fixture_path('nested_file2.json'))] == nested


def test_nested_yml():
    assert [generate_diff(get_fixture_path('nested_file1.yml'),
                          get_fixture_path('nested_file2.yml'))] == nested


def test_plain_formatter():
    expected = plain_data
    assert [generate_diff(get_fixture_path('nested_file1.json'),
                          get_fixture_path('nested_file2.yml'), 'plain')] == expected


def test_is_json():
    assert json.loads(generate_diff(get_fixture_path('nested_file1.json'),
                      get_fixture_path('nested_file2.yml'), 'json'))
