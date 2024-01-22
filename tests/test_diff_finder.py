import json
from gendiff.diff_finder import diff_finder

def test_generate_diff():
    assert  generate_diff(path_to_file1, path_to_file2) == {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}

