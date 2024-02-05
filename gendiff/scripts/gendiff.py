#!/usr/bin/env python3


import argparse
from gendiff.cli import get_parser_args
import json
from gendiff.diff_finder import generate_diff


def main():
    args = get_parser_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()

