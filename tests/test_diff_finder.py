import json
import yaml
import pytest
from gendiff.diff_finder import generate_diff
# from tests.fixtures.expected_results import result



def test_generate_diff():
    with open("./tests/fixtures/expected_results.txt", 'r', encoding='utf8') as file:
        # result = file.read().strip('\n')
        result = file.read()
        assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json', stylish) == result
