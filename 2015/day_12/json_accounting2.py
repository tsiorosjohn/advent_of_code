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
        document = f.read()
        # pprint(document)

    # Part Two
    def no_red(obj):
        """Evaluate json objects adding numbers not in dicts containing "red"."""
        if type(obj) == int:
            # print(f"{obj = }")
            return obj
        if type(obj) == list:
            return sum([no_red(item) for item in obj])
        if type(obj) == dict:
            if 'red' in obj.values():
                return 0
            return no_red(list(obj.values()))
        return 0


    # Answer Two
    print("Corrected Sum =", no_red(json.loads(document)))

