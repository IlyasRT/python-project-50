from gendiff.generate_diff import generate_diff


def test_generate_diff():
    with open(
        "./tests/fixtures/expected_results_2.txt", 'r', encoding='utf8'
    ) as file:
        result = file.read().strip('\n')
        assert generate_diff(
            './tests/fixtures/file-1.json',
            './tests/fixtures/file-2.json', 'stylish'
        ) == result
