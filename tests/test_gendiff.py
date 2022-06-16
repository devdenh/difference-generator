from gendiff import generate_diff
import json
from tests.fixtures.expected import expected_for_flat_diff_json
from tests.fixtures.expected import expected_for_nested_diff_json
from tests.fixtures.expected import get_fixture_path
from tests.fixtures.expected import plain_data


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


def test_is_str_nested_yml():
    assert isinstance(generate_diff(get_fixture_path('nested_file1.yml'),
                      get_fixture_path('nested_file2.yml')), str)


nested = expected_for_nested_diff_json()


def test_nested_json():
    assert generate_diff(get_fixture_path('nested_file1.json'),
                         get_fixture_path('nested_file2.json')) == nested


def test_nested_yml():
    assert generate_diff(get_fixture_path('nested_file1.yml'),
                         get_fixture_path('nested_file2.yml')) == nested


def test_plain_formatter():
    expected = plain_data
    assert generate_diff(get_fixture_path('nested_file1.json'),
                         get_fixture_path('nested_file2.yml'), 'plain') == expected


def test_is_json():
    assert json.loads(generate_diff(get_fixture_path('nested_file1.json'),
                      get_fixture_path('nested_file2.yml'), 'json'))
