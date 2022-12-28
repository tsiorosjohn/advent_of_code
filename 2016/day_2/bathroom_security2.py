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
    x, y = 2, 0
    for count, line_f in enumerate(lines_f):
        # print(f"{keypad[x][y] = }")
        for char in line_f:
            if char == 'U' and (x != 0 and keypad[x-1][y] != 0):
                x -= 1
            elif char == 'D' and (x != 4 and keypad[x+1][y] != 0):
                x += 1
            elif char == 'L' and (y != 0 and keypad[x][y-1] != 0):
                y -= 1
            elif char == 'R' and (y != 4 and keypad[x][y+1] != 0):
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

    keypad2 = [[0, 0,  1,  0, 0],
               [0, 2,  3,  4, 0],
               [5, 6,  7,  8, 9],
               [0,'A','B','C',0],
               [0, 0, 'D', 0, 0]]


    # get_instructions(lines, keypad)
    get_instructions(lines, keypad2)

