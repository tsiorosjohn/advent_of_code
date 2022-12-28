import copy
import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_instructions(lines_f, keypad):
    x, y = 1, 1
    for count, line_f in enumerate(lines_f):
        for char in line_f:
            if char == 'U' and x != 0:
                x -= 1
            elif char == 'D' and x != 2:
                x += 1
            elif char == 'L' and y != 0:
                y -= 1
            elif char == 'R' and y != 2:
                y += 1
        print(f"{count = } // {x = }, {y = } //// {keypad[x][y] = }")


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    get_instructions(lines, keypad)

