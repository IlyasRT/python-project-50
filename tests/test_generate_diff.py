from gendiff.generate_diff import generate_diff
import pytest
import os

''' 
def test_generate_diff():
    with open(
        "./tests/fixtures/expected_results.txt", 'r', encoding='utf8'
    ) as file:
        result = file.read().strip('\n')
        assert generate_diff(
            './tests/fixtures/file1.json',
            './tests/fixtures/file2.json', 'stylish'
        ) == result
'''
        
@pytest.mark.parametrize('file_1_name, file_2_name, formatter', [
    ('file-1.json', 'file-2.json', 'stylish'),
    ('file-1.yml', 'file-2.yml', 'stylish'),
    ('file-1.json', 'file-2.json', 'plain'),
    ('file-1.yml', 'file-2.yml', 'plain'),
    ('file-1.json', 'file-2.json', 'json'),
    ('file-1.yml', 'file-2.yml', 'json')
])


from gendiff.generator_diff import generate_diff


def test_generate_stylish():
    diff_json_stylish = generate_diff(
        "tests/fixtures/file-1.json", "tests/fixtures/file-2.json", "stylish"
    )
    diff_yaml_stylish = generate_diff(
        "tests/fixtures/file-1.yaml", "tests/fixtures/file-2.yaml", "stylish"
    )
    diff_yml_stylish = generate_diff(
        "tests/fixtures/file-1.yml", "tests/fixtures/file-2.yml", "stylish"
    )
    result_stylish = open("tests/fixtures/expected_results_stylish.txt").read()

    assert diff_json_stylish == result_stylish
    assert diff_yaml_stylish == result_stylish
    assert diff_yml_stylish == result_stylish


def test_generate_plain():
    diff_json_plain = generate_diff(
        "tests/fixtures/file-1.json", "tests/fixtures/file-2.json", "plain"
    )
    diff_yaml_plain = generate_diff(
        "tests/fixtures/file-1.yaml", "tests/fixtures/file-2.yaml", "plain"
    )
    diff_yml_plain = generate_diff(
        "tests/fixtures/file-1.yml", "tests/fixtures/file-2.yml", "plain"
    )
    result_plain = open("tests/fixtures/expected_results_plain.txt").read()

    assert diff_json_plain == result_plain
    assert diff_yaml_plain == result_plain
    assert diff_yml_plain == result_plain


def test_generate_json():
    diff_json_json = generate_diff(
        "tests/fixtures/file-1.json", "tests/fixtures/file-2.json", "json"
    )
    diff_yaml_json = generate_diff(
        "tests/fixtures/file-1.yaml", "tests/fixtures/file-2.yaml", "json"
    )
    diff_yml_json = generate_diff(
        "tests/fixtures/file-1.yml", "tests/fixtures/file-2.yml", "json"
    )
    result_json = open("tests/fixtures/expected_results_json.txt).read()

    assert diff_json_json == result_json
    assert diff_yaml_json == result_json
    assert diff_yml_json == result_json
