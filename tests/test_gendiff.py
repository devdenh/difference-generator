from gendiff import generate_diff
import json
import pytest
import os


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


def test_flatdiff(file1_json, file2_json):
    start = '{'
    end = '}'
    expected = (f'{start}\n  '
                f'- follow: false\n  '
                f'  host: hexlet.io\n  '
                f'- proxy: 123.234.53.22\n  '
                f'- timeout: 50\n  '
                f'+ timeout: 20\n  '
                f'+ verbose: true\n'
                f'{end}')
    assert generate_diff(file1_json, file2_json) == expected


def test_is_string(file1_json, file2_json):
    assert isinstance(generate_diff(file1_json, file2_json), str)
