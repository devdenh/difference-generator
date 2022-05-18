from gendiff import generate_diff
import json
import yaml
import pytest
from tests.fixtures.expected import expected_for_flat_diff_json


@pytest.fixture(scope='module')
def file1_json(tmpdir_factory):
    python_file1_data = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }

    file1 = tmpdir_factory.mktemp('data').join('python_file1_data')

    with file1.open('w') as f:
        json.dump(python_file1_data, f)
    return file1


@pytest.fixture(scope='module')
def file2_json(tmpdir_factory):
    python_file2_data = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }

    file2 = tmpdir_factory.mktemp('data').join('python_file2_data')

    with file2.open('w') as f:
        json.dump(python_file2_data, f)
    return file2


@pytest.fixture(scope='module')
def file1_yml(tmpdir_factory):
    python_file1_data = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }

    file1 = tmpdir_factory.mktemp('data').join('python_file1_data')

    with file1.open('w') as f:
        yaml.dump(python_file1_data, f)
    return file1


@pytest.fixture(scope='module')
def file2_yml(tmpdir_factory):
    python_file2_data = {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }

    file2 = tmpdir_factory.mktemp('data').join('python_file2_data')

    with file2.open('w') as f:
        yaml.dump(python_file2_data, f)
    return file2


def test_flatdiff_json(file1_json, file2_json):
    expected = expected_for_flat_diff_json()
    assert generate_diff(file1_json, file2_json) == expected


def test_is_string(file1_json, file2_json):
    assert isinstance(generate_diff(file1_json, file2_json), str)


def test_flatdiff_yaml(file1_yml, file2_yml):
    expected = expected_for_flat_diff_json()
    assert generate_diff(file1_yml, file2_yml) == expected
