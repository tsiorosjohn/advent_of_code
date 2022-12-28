import copy
import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def calc_instructions(lines_f):
    a, b = 0, 0

    def register_calc(line, af, bf):
        if 'a' in line:
            return 'a', af
        elif 'b' in line:
            return 'b', bf
        else:
            return 'j', None

    temp = 0
    for l in lines_f:
        if register_calc(l, a, b)[1]:
            temp = register_calc(l, a, b)[1]
        register = register_calc(l, a, b)[0]
        if 'hlf' in l:
            temp = temp / 2
            print(f"{register = } //  {temp = } - hlf  ")
        elif 'tpl' in l:
            temp = temp * 3
            print(f"{register = } //  {temp = } - tpl  ")
        elif 'inc' in l:
            temp += 1
            print(f"{register = } //  {temp = } - inc  ")
        elif 'inc' in l:
            temp += 1
            print(f"{register = } //  {temp = } - inc  ")



if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)

    # get all lines in list from input
    print(lines, len(lines))
    calc_instructions(lines)
