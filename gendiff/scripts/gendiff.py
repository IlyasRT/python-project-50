import argparse
import json
from gendiff.cli import get_arg
from gendiff.diff_finder import generate_diff

def main():
    file1, file2 = cli.get_arg()
    result = generate_diff(file1, file2)
    print(result)
    
    

if __name__ == '__main__':
    main()
