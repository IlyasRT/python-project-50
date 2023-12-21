import argparse
import json


def get_arg():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f FORMAT, --format FORMAT set format of output')
    args = parser.parse_args()
    # return a_1, a_2, a_3
