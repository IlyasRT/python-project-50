#!/usr/bin/env python3


import argparse
from gendiff.cli import get_parser_args
import json
from gendiff.diff_finder import generate_diff
from gendiff.parser import parse_data_from_file


def main():
    args = get_parser_args()
    # print('args=',args)
    diff = generate_diff(args.first_file, args.second_file, args.format)
    # print('контрольная точка --> прошел определение функции diff')
    print(diff)


if __name__ == '__main__':
    main()

