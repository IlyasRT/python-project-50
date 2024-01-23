import json
from gendiff.diff_finder import generate_diff

def test_generate_diff():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}
    
    

    
'''
def test_generate_diff():
    assert generate_diff('./fixtures/file1.json', './fixtures/file2.json') == {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}


    assert generate_diff(file1.json, file2.json) == {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}


def test_generate_diff():
    assert  generate_diff(./tests/fixtures/file1.json, ./tests/fixtures/file2.json) == {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}

def test_generate_diff():
    assert  generate_diff(/fixtures/file1.json, /fixtures/file2.json) == {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}
    
def test_generate_diff():
    assert  generate_diff(./fixtures/file1.json, ./fixtures/file2.json) == {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}

def test_generate_diff():
    assert  generate_diff(fixtures/file1.json, fixtures/file2.json) == {' - follow': False, 'host': 'hexlet.io', ' - proxy': '123.234.53.22', ' - timeout': 50, ' + timeout': 20, ' + verbose': True}

'''


