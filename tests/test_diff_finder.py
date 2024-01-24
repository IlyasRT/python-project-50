import json
from gendiff.diff_finder import generate_diff
import test.fixtures.expected_comparison_result



def test_generate_diff():

    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result = {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}

    # assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == expected_comparison_result.result
