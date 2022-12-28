import itertools
import re
from pprint import pprint


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def calculate_next(input):
    print(f"================= {input} ================")
    next = ''
    temp = 1
    for i in range(len(input)):
        if i == 0:
            next = next + str(temp * input[i])
            print(f"i: {i}, current char: {input[i]}, {temp = } - {next=}")
        elif i >= 1:
            print(f"i: {i}, current char: {input[i]}, previous char: {input[i-1]}")
            if input[i] == input[i-1]:
                temp += 1
                print(f"    char equal: {input[i]}, {temp = }")
            else:
                # next = str(temp * input[i]) + next
                next = str(temp * input[i]) + next
        if i == len(input)-1:
            next = next + str(temp * input[i])
        # else:
        #     print(f"i: {i}, current char: {input[i]}, {temp = }")
        #     next = next + str(temp * input[i])
    print(f"next: {next}")


if __name__ == "__main__":
    # file = 'input.txt'
    file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    for line in lines:
        calculate_next(line)