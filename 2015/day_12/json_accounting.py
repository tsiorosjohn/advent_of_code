import itertools
import re
from pprint import pprint
from string import ascii_lowercase
import json


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    # print(lines)

    with open(file) as f:
        file_json = json.load(f)
        # pprint(file_json)
        file_string = f.readlines()
        # for line in file_string:
        #     print(line)
        # print(file_string)

    # print(lines)
    for line in lines:
        re_find = re.findall(r'-?[0-9]+', line)

    sum = 0
    for item in re_find:
        sum += int(item)
    print(sum)
