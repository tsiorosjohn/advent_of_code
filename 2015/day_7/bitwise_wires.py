import re
from pprint import pprint


def parse_input(file1):
    input_ls = []
    with open(file1) as reader:
        flines = reader.readlines()
        for item in flines:
            input_ls.append(item.rstrip())
    return input_ls


def calculate_bitwise(ls):
    wires = {}

    def find_items_with_value():
        # find first items that have already a value:
        for line in ls:
            field = line.split()
            if len(field) == 3:
                # print(line)
                if line_regex := re.search(r'([0-9,]+) -> ([a-z,]+)', line):  # more advanced via regex // actually not needed...
                    # print(line, '=====', line_regex)
                    # print(line)
                    wires[field[2]] = field[0]
        print(f" intermediate {wires = }")
        # continue with bitwise after replacing variables with values:

    def calculation_part(line_f, field, a_side, b_side):
        print(f"{line_f = }")
        if 'AND' in line_f:
            print(f"ANDD {line_f, a_side, b_side}")
            wires[field[4]] = a_side & b_side
        elif 'OR' in line_f:
            wires[field[4]] = a_side | b_side
        elif 'LSHIFT' in line_f:
            wires[field[4]] = a_side << b_side
        elif 'RSHIFT' in line_f:
            wires[field[4]] = a_side >> b_side
        elif 'NOT' in line_f:
            temp = int(wires[field[1]])
            binary_value = bin(temp)[2:].zfill(16)
            not_binary = ''
            for bit in binary_value:
                if bit == '1':
                    not_binary += '0'
                else:
                    not_binary += '1'
            value = int(not_binary, 2)
            print('value ', value)
            wires[field[3]] = value
            # print(wires[field[0]], wires[field[2]])
            # wires[field[4]] = wires[field[0]] + wires[field[2]]
        print(f"{wires = }")

    find_items_with_value()

    def check_whole_list():
        # first pass, both numbers with values:
        for line in ls:
            field = line.split()
            print(f"{field = }")
            # if re.search(r'[0-9]{1-2}', field[0]) and re.search(r'[0-9]{1-2}', field[2]):
            if field[0].isnumeric() and field[2].isnumeric():
                print('Already numbers for both xxxxx ', line)
                a_side = int(field[0])
                b_side = int(field[2])
                calculation_part(line, field, a_side, b_side)
            elif field[0].isnumeric():
                print('Already number for field 0 xxxxx ', line)
                a_side = int(field[0])
                if field[2] in wires:
                    b_side = int(wires[field[2]])
                    calculation_part(line, field, a_side, b_side)
                else:
                    continue
                    # find_items_with_value()
            elif field[2].isnumeric():
                print('Already number for field 2 xxxxx ', line)
                if field[0] in wires:
                    a_side = int(wires[field[0]])
                    b_side = int(field[2])
                    calculation_part(line, field, a_side, b_side)
                else:
                    continue
                    # find_items_with_value()
                    # calculation_part(line)
            elif len(field) != 4:  # exluding NOT scenario from calculations
                print('neither a or b is  numeric!')
                if field[0] in wires and field[2] in wires:
                    # if field[0].isnumeric() and field[2].isnumeric():
                    a_side = int(wires[field[0]])
                    b_side = int(wires[field[2]])
                    calculation_part(line, field, a_side, b_side)
                else:
                    continue
                # find_items_with_value()
                    # calculation_part(line)
            elif len(field) == 4:
                if field[1] in wires:
                    calculation_part(line, field, a_side, b_side)
                else:
                    continue
                    # find_items_with_value()
                print(f'notcase {field = }')

    for i in range(len(wires)):
        check_whole_list()


    return wires


if __name__ == "__main__":
    file = 'input.txt'
    # file = 'example.txt'
    lines = parse_input(file)
    print(lines)

    w1 = calculate_bitwise(lines)
    print(w1)

    # print(w1[e])