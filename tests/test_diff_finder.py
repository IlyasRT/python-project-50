import json
from gendiff.diff_finder import generate_diff
from tests.expected_results import result



def test_generate_diff():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result
