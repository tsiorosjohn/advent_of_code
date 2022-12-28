import copy
import re


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def get_destination(ls):
    degrees = 0
    x, y = 0, 0

    def get_destinations(deg, x, y, len):
        if (deg % 360) / 90 == 0:  # north
            return x, y+len
        elif (deg % 360) / 90 == 1:  # east
            return x+len, y
        elif (deg % 360) / 90 == 2:  # south
            return x, y-len
        elif (deg % 360) / 90 == 3:  # west
            return x-len, y

    for instruction in ls:
        if 'L' in instruction:
            degrees -= 90
            x, y = get_destinations(degrees, x, y, int(instruction[1:]))
        elif 'R' in instruction:
            degrees += 90
            x, y = get_destinations(degrees, x, y, int(instruction[1:]))

    return x, y


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    # file = 'example2.txt'
    # lines = parse_input(file)
    # print(lines[0].replace(" ", ''))
    lines = parse_input(file)[0].replace(" ", "").split(',')

    # get all lines in list from input
    print(lines, len(lines))
    x, y = get_destination(lines)
    print(f"{x, y = } // {abs(x) + abs(y) = }")
    # print(get_destination(lines))

