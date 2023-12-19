import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Cmpares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f FORMAT, --format FORMAT set format of output')
    args = parser.parse_args()
    # 111 print(args.filename, args.count, args.verbose)


def generate_diff(path_to_file1, path_to_file2):
    content_file_1 = json.load(open(path_to_file1))
    content_file_2 = json.load(open(path_to_file2))
    content_file_3 = {}
    for k, v in sorted(content_file_1.items()):
        if k not in content_file_2:
            k =' - ' + str(k)
            content_file_3[k] = v
        if k in content_file_2 and content_file_1[k] != content_file_2[k]:
            content_file_3[' - ' + str(k)] = v
            content_file_3[' + ' + str(k)] = content_file_2[k]
        if k in content_file_2 and content_file_1[k] == content_file_2[k]:
            content_file_3[k] = v
        if k in content_file_2 and content_file_1[k] == content_file_2[k]:
            content_file_3[k] = v
    key_not_in_content_file_1 = list(set(content_file_2).difference(set(content_file_1)))
    for i in key_not_in_content_file_1:
        if i in content_file_2:
            content_file_3[' + '+str(i)] = content_file_2[i]
    return content_file_3

if __name__ == '__main__':
    main()
