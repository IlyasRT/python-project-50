from gendiff.generate_diff import generate_diff
# import pytest
# import os



@pytest.mark.parametrize('path_to_file1, path_to_file2, expected_result', [
    ('./tests/fixtures/file-1.json', './tests/fixtures/file-2.json', 'expected_results_stylish.txt'),
    ('./tests/fixtures/file-1.yml', './tests/fixtures/file-2.yml', 'expected_results_stylish.txt'),
    ('./tests/fixtures/file-1.json', './tests/fixtures/file-2.json', 'expected_results_plain.txt'),
    ('./tests/fixtures/file-1.yml', './tests/fixtures/file-2.yml', 'expected_results_plain.txt'),
    ('./tests/fixtures/file-1.json', './tests/fixtures/file-2.json', 'expected_results_json.txt'),
    ('./tests/fixtures/file-1.yml', './tests/fixtures/file-2.yml', 'expected_results_json.txt')
])


'''
def test_generate_stylish():
    diff_json_stylish = generate_diff(
        "./tests/fixtures/file-1.json",
        "./tests/fixtures/file-2.json", "stylish"
    )
    diff_yml_stylish = generate_diff(
        "./tests/fixtures/file-1.yml", "./tests/fixtures/file-2.yml", "stylish"
    )
    with open(
        "./tests/fixtures/expected_results_stylish.txt", 'r', encoding='utf8'
    ) as file:
        result_stylish = file.read().strip('\n')
        assert diff_json_stylish == result_stylish
        assert diff_yml_stylish == result_stylish
'''

def test_gendiff_stylish(path_to_file1, path_to_file2, expected_result):
    diff = generate_diff(file1, file2, format="stylish")
    assert diff == read_file(expected_result)
'''

def test_generate_plain():
    diff_json_plain = generate_diff(
        "./tests/fixtures/file-1.json", "./tests/fixtures/file-2.json", "plain"
    )
    diff_yml_plain = generate_diff(
        "./tests/fixtures/file-1.yml", "./tests/fixtures/file-2.yml", "plain"
    )
    with open(
        "./tests/fixtures/expected_results_plain.txt", 'r', encoding='utf8'
    ) as file:
        result_plain = file.read().strip('\n')
        assert diff_json_plain == result_plain
        assert diff_yml_plain == result_plain


def test_generate_json():
    diff_json_json = generate_diff(
        "./tests/fixtures/file-1.json", "./tests/fixtures/file-2.json", "json"
    )
    diff_yml_json = generate_diff(
        "./tests/fixtures/file-1.yml", "./tests/fixtures/file-2.yml", "json"
    )
    with open(
        "./tests/fixtures/expected_results_json.txt", 'r', encoding='utf8'
    ) as file:
        result_json = file.read().strip('\n')
        assert diff_json_json == result_json
        assert diff_yml_json == result_json
