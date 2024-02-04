import json
import pytest
from gendiff.diff_finder import generate_diff
#from tests.fixtures.expected_results import result


'''
Вариант 0 - использовал для теста, чтобы проверить все остальное кроме импорта expected_results.txt
result = {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}
def test_generate_diff():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result
'''


#Вариант 1 - для полного сравнения мешают двойные кавычки  перед знаком {
def test_generate_diff():
    with open("./tests/fixtures/expected_results.txt", 'r', encoding='utf8') as file:
        result = file.read().strip('\n')
        assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result

'''
Вариант 2 - не прошел тесты понял позже что json.load используется только при открытии файлов в вида *.json

def test_generate_diff():
    result = json.load(open("./tests/fixtures/expected_results.txt")) #  загружает json и выгружает в виде строки, но тоже не проходит тесты
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result
'''
