import json
from gendiff.diff_finder import generate_diff
#from tests.fixtures.expected_results import result


def test_generate_diff():
    with open("./tests/fixtures/expected_results.txt", encoding='utf8') as file:
        result = file.read()
        print(result)
        result_json = json.loads(result)
        print(result_json)

    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == result_json
    
    
    
# для тестов оставил 
# result = {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}
        
