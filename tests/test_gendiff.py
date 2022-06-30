from gendiff import generate_diff
import json
from tests.fixtures.expected import get_fixture_path


def test_is_string():
    assert isinstance(generate_diff(get_fixture_path('file1.json'),
                      get_fixture_path('file2.json')), str)


def test_is_string_yml():
    assert isinstance(generate_diff(get_fixture_path('file1.yml'),
                      get_fixture_path('file2.yml')), str)


def test_is_json():
    assert json.loads(generate_diff(get_fixture_path('file1.json'),
                      get_fixture_path('file2.yml'), 'json'))
